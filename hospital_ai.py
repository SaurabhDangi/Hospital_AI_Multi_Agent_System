
import os
import sqlite3
import pandas as pd
import faiss
# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "hospital.db"
)

DOCUMENTS_PATH = os.path.join(
    BASE_DIR,
    "documents"
)
print("Database path:", DB_PATH)
print("Database exists:", os.path.exists(DB_PATH))

from sentence_transformers import SentenceTransformer
from google import genai


# ==========================================
# 1. GEMINI CLIENT
# ==========================================

gemini_api_key = os.environ.get("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

gemini_client = genai.Client(
    api_key=gemini_api_key
)


# ==========================================
# 2. DATABASE SCHEMA
# ==========================================

schema = """
Database table: patients

Columns:
- Name
- Age
- Gender
- Blood Type
- Medical Condition
- Date of Admission
- Doctor
- Hospital
- Insurance Provider
- Billing Amount
- Room Number
- Admission Type
- Discharge Date
- Medication
- Test Results
"""


# ==========================================
# 3. SQL FUNCTIONS
# ==========================================

def generate_sql(question):

    prompt = f"""
You are an SQL expert.

Convert the user's natural language question
into a SQLite SQL query.

Database schema:

{schema}

Rules:
1. Use only the patients table.
2. Use only columns from the schema.
3. Generate READ-ONLY SQL.
4. Return ONLY the SQL query.
5. Do not use markdown.
6. Do not explain anything.

Question:
{question}
"""

    response = gemini_client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text.strip()


def validate_sql(sql):

    sql_lower = sql.strip().lower()

    if not sql_lower.startswith(("select", "with")):
        raise ValueError(
            "Only read-only SQL queries are allowed."
        )

    forbidden = [
        "drop",
        "delete",
        "update",
        "insert",
        "alter",
        "create",
        "replace"
    ]

    for command in forbidden:

        if command in sql_lower:
            raise ValueError(
                f"Unsafe SQL detected: {command}"
            )

    return True


def run_sql(query):

    connection = sqlite3.connect(DB_PATH)

    try:
        result = pd.read_sql_query(
            query,
            connection
        )
    finally:
        connection.close()

    return result


def sql_agent(question):

    sql = generate_sql(question)

    validate_sql(sql)

    result = run_sql(sql)

    return {
        "agent": "NLP-to-SQL Agent",
        "sql": sql,
        "result": result
    }


def format_sql_answer(question, result):

    if result.empty:
        return "No matching records were found."

    value = result.iloc[0, 0]

    question_lower = question.lower()

    if "how many" in question_lower:

        return f"There are {int(value):,} matching patients."

    if "average age" in question_lower:

        return f"The average patient age is {float(value):.1f} years."

    if "average billing" in question_lower:

        return f"The average billing amount is ${float(value):,.2f}."

    return f"The result is {value}."


# ==========================================
# 4. LOAD POLICY DOCUMENTS
# ==========================================

documents = []

for filename in os.listdir(DOCUMENTS_PATH):

    if filename.endswith(".txt"):

        filepath = os.path.join(
            DOCUMENTS_PATH,
            filename
        )

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

        documents.append({
            "filename": filename,
            "text": text
        })


# ==========================================
# 5. CREATE CHUNKS
# ==========================================

chunks = []

for doc in documents:

    paragraphs = doc["text"].split("\n\n")

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if paragraph:

            chunks.append({
                "filename": doc["filename"],
                "text": paragraph
            })


# ==========================================
# 6. EMBEDDINGS
# ==========================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

texts = [
    chunk["text"]
    for chunk in chunks
]

embeddings = embedding_model.encode(
    texts,
    convert_to_numpy=True
)


# ==========================================
# 7. FAISS
# ==========================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)


# ==========================================
# 8. RETRIEVAL
# ==========================================

def retrieve_documents(
    question,
    top_k=3
):

    question_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        question_embedding,
        top_k
    )

    results = []

    for i in indices[0]:

        results.append(chunks[i])

    return results


# ==========================================
# 9. RAG
# ==========================================

def generate_rag_answer(
    question,
    retrieved_chunks
):

    context = "\n\n".join(
        [
            f"Source: {chunk['filename']}\n"
            f"{chunk['text']}"
            for chunk in retrieved_chunks
        ]
    )

    prompt = f"""
You are a hospital policy assistant.

Answer the user's question using ONLY
the hospital policy information below.

Question:
{question}

Policy information:
{context}

Rules:
1. Answer clearly and concisely.
2. Do not invent information.
3. Do not provide medical advice.
4. If the answer is not available, say:
"The available hospital policies do not contain
this information."
"""

    response = gemini_client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text.strip()


def rag_agent(question):

    retrieved_chunks = retrieve_documents(
        question,
        top_k=3
    )

    answer = generate_rag_answer(
        question,
        retrieved_chunks
    )

    return {
        "agent": "RAG Agent",
        "answer": answer,
        "sources": retrieved_chunks
    }


# ==========================================
# 10. ORCHESTRATOR
# ==========================================

def classify_question(question):

    prompt = f"""
You are the routing agent for a hospital AI assistant.

Classify the user's question into exactly ONE:

DATABASE
POLICY

DATABASE = patient records/data.

POLICY = hospital rules/procedures.

Return ONLY:
DATABASE
or
POLICY

Question:
{question}
"""

    response = gemini_client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    route = response.text.strip().upper()

    if "DATABASE" in route:
        return "DATABASE"

    if "POLICY" in route:
        return "POLICY"

    raise ValueError(
        "Unable to classify question."
    )


def hospital_assistant(question):

    route = classify_question(question)

    if route == "DATABASE":

        result = sql_agent(question)

        return {
            "route": route,
            "agent": "NLP-to-SQL Agent",
            "answer": format_sql_answer(
                question,
                result["result"]
            ),
            "sql": result["sql"],
            "sources": []
        }

    else:

        result = rag_agent(question)

        return {
            "route": route,
            "agent": "RAG Agent",
            "answer": result["answer"],
            "sql": None,
            "sources": result["sources"]
        }
