import streamlit as st
import hospital_ai
import textwrap

st.title("🔥 NEW VERSION TEST")

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Hospital AI Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    textwrap.dedent("""
    <style>

    /* =========================
       GLOBAL
       ========================= */

    .stApp {
        background: #0e1117;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* =========================
       HEADER
       ========================= */

    .main-header {
        padding: 25px 30px;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            #151a23,
            #1c2430
        );
        border: 1px solid #2b3442;
        margin-bottom: 30px;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 17px;
        color: #aeb7c4;
        margin-bottom: 18px;
    }

    .status {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 20px;
        background: #123c2a;
        color: #4ade80;
        font-size: 14px;
        font-weight: 600;
    }


    /* =========================
       SECTION TITLES
       ========================= */

    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 25px;
        margin-bottom: 15px;
    }


    /* =========================
       AGENT CARDS
       ========================= */

    .agent-card {
        min-height: 190px;
        padding: 24px;
        border-radius: 16px;
        background: #151a23;
        border: 1px solid #2b3442;
        transition: 0.2s;
    }

    .agent-card:hover {
        border-color: #4f8cff;
        transform: translateY(-2px);
    }

    .agent-icon {
        font-size: 32px;
        margin-bottom: 12px;
    }

    .agent-title {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }

    .agent-description {
        font-size: 14px;
        line-height: 1.6;
        color: #aeb7c4;
    }


    /* =========================
       QUERY BOX
       ========================= */

    .query-container {
        margin-top: 30px;
        padding: 25px;
        border-radius: 18px;
        background: #151a23;
        border: 1px solid #2b3442;
    }


    /* =========================
       RESULT CARD
       ========================= */

    .result-card {
        padding: 25px;
        border-radius: 18px;
        background: #151a23;
        border: 1px solid #2b3442;
        margin-top: 25px;
    }

    .result-label {
        font-size: 14px;
        color: #8b98a9;
        margin-bottom: 5px;
    }

    .result-answer {
        font-size: 22px;
        font-weight: 600;
        color: #ffffff;
        line-height: 1.5;
    }


    /* =========================
       AGENT BADGE
       ========================= */

    .agent-badge {
        display: inline-block;
        padding: 8px 15px;
        border-radius: 20px;
        background: #123c2a;
        color: #4ade80;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 15px;
    }


    /* =========================
       SIDEBAR
       ========================= */

    [data-testid="stSidebar"] {
        background: #11151c;
        border-right: 1px solid #252c36;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 20px;
    }

    .sidebar-agent {
        padding: 10px 0;
        color: #c4ccd6;
        font-size: 15px;
    }

    .sidebar-info {
        margin-top: 25px;
        padding: 15px;
        border-radius: 12px;
        background: #182b44;
        color: #9ec5ff;
        font-size: 13px;
        line-height: 1.5;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid #252c36;
        color: #6f7b8a;
        font-size: 13px;
    }

    </style>
    """),
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        textwrap.dedent("""
        <div class="sidebar-title">
            🏥 Hospital AI
        </div>
        """),
        unsafe_allow_html=True
    )

    st.write("### 🤖 Multi-Agent System")

    st.markdown(
        """
        <div class="sidebar-agent">🧠 Orchestrator Agent</div>
        <div class="sidebar-agent">🗄️ NLP-to-SQL Agent</div>
        <div class="sidebar-agent">📚 RAG Agent</div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.write("### System")

    st.write("🟢 AI System Online")
    st.write("🗃️ SQLite Database")
    st.write("🔎 FAISS Retrieval")
    st.write("✨ Gemini AI")

    st.markdown(
        textwrap.dedent("""
        <div class="sidebar-info">
            Patient data is synthetic and used only
            for demonstration purposes.
        </div>
        """),
        unsafe_allow_html=True
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="main-header">

        <div class="main-title">
            🏥 Hospital AI Assistant
        </div>

        <div class="subtitle">
            Intelligent multi-agent assistant for patient
            records and hospital policy information.
        </div>

        <div class="status">
            ● AI System Online
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


# =========================================================
# MULTI-AGENT ARCHITECTURE
# =========================================================

st.markdown(
    '<div class="section-title">🤖 Multi-Agent Architecture</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        textwrap.dedent("""
        <div class="agent-card">

            <div class="agent-icon">
                🧠
            </div>

            <div class="agent-title">
                Orchestrator
            </div>

            <div class="agent-description">
                Understands the user's question and routes
                it to the appropriate specialist agent.
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        textwrap.dedent("""
        <div class="agent-card">

            <div class="agent-icon">
                🗄️
            </div>

            <div class="agent-title">
                NLP-to-SQL
            </div>

            <div class="agent-description">
                Converts natural language questions into
                safe read-only SQLite queries.
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        textwrap.dedent("""
        <div class="agent-card">

            <div class="agent-icon">
                📚
            </div>

            <div class="agent-title">
                RAG Agent
            </div>

            <div class="agent-description">
                Retrieves relevant information from hospital
                policy documents using semantic search.
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


# =========================================================
# QUESTION SECTION
# =========================================================

st.markdown(
    '<div class="section-title">💬 Ask the Hospital AI</div>',
    unsafe_allow_html=True
)

question = st.text_input(
    "Your question",
    placeholder="Example: How many patients have diabetes?",
    label_visibility="collapsed"
)


ask_button = st.button(
    "🚀 Ask AI",
    type="primary",
    use_container_width=True
)


# =========================================================
# PROCESS QUESTION
# =========================================================

if ask_button:

    if not question.strip():

        st.warning(
            "Please enter a question before clicking Ask AI."
        )

    else:

        with st.spinner(
            "🤖 Analyzing your question..."
        ):

            try:

                response = hospital_ai.hospital_assistant(
                    question
                )

                # =================================================
                # SELECTED AGENT
                # =================================================

                st.markdown(
                    f"""
                    <div class="agent-badge">
                        ✓ Selected Agent: {response["agent"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # =================================================
                # ANSWER
                # =================================================

                st.markdown(
                    textwrap.dedent("""
                    <div class="result-card">

                        <div class="result-label">
                            AI RESPONSE
                        </div>

                    </div>
                    """),
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="result-answer">
                        {response["answer"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # =================================================
                # ROUTING DETAILS
                # =================================================

                with st.expander(
                    "🔍 View routing details"
                ):

                    st.write(
                        "**Route:**",
                        response["route"]
                    )


                    # =============================================
                    # SQL
                    # =============================================

                    if response.get("sql"):

                        st.write(
                            "**Generated SQL:**"
                        )

                        st.code(
                            response["sql"],
                            language="sql"
                        )


                    # =============================================
                    # RAG SOURCES
                    # =============================================

                    if response.get("sources"):

                        st.write(
                            "**Sources:**"
                        )

                        unique_sources = []

                        for source in response["sources"]:

                            filename = source.get(
                                "filename"
                            )

                            if (
                                filename
                                and
                                filename not in unique_sources
                            ):

                                unique_sources.append(
                                    filename
                                )

                        for filename in unique_sources:

                            st.write(
                                f"📄 {filename}"
                            )


            except Exception as e:

                st.error(
                    f"An error occurred: {str(e)}"
                )


# =========================================================
# EXAMPLE QUESTIONS
# =========================================================

st.markdown(
    '<div class="section-title">💡 Try asking</div>',
    unsafe_allow_html=True
)

example_col1, example_col2, example_col3 = st.columns(3)


with example_col1:

    st.info(
        "🩺 **Patient Data**\n\n"
        "How many patients have diabetes?"
    )


with example_col2:

    st.info(
        "🏥 **Hospital Policy**\n\n"
        "What are the hospital visiting hours?"
    )


with example_col3:

    st.info(
        "💰 **Database Query**\n\n"
        "What is the average billing amount?"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="footer">
        🏥 Hospital AI Assistant
        &nbsp; • &nbsp;
        Multi-Agent AI System
        &nbsp; • &nbsp;
        Synthetic Data for Demonstration
    </div>
    """),
    unsafe_allow_html=True
)
