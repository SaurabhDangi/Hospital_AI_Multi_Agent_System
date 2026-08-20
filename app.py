import streamlit as st
import hospital_ai


# =========================================================
# PAGE CONFIG
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
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #0e1117;
    }

    /* Main content width */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .main-header {
        padding: 1rem 0 2rem 0;
    }

    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        color: #9ca3af;
        font-size: 1.05rem;
    }

    /* Status */
    .status {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 20px;
        background-color: #123524;
        color: #4ade80;
        font-size: 0.85rem;
        margin-top: 0.8rem;
    }

    /* Agent cards */
    .agent-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 1.1rem;
        min-height: 120px;
    }

    .agent-icon {
        font-size: 1.5rem;
    }

    .agent-title {
        font-weight: 600;
        font-size: 1rem;
        margin-top: 0.4rem;
    }

    .agent-description {
        color: #8b949e;
        font-size: 0.85rem;
        margin-top: 0.3rem;
    }

    /* Section headings */
    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 0.8rem;
    }

    /* Answer card */
    .answer-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 14px;
        padding: 1.4rem;
        margin-top: 1rem;
    }

    .answer-label {
        color: #8b949e;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .answer-text {
        font-size: 1.15rem;
        margin-top: 0.5rem;
        line-height: 1.6;
    }

    /* Agent badge */
    .agent-badge {
        display: inline-block;
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 20px;
        padding: 0.4rem 0.8rem;
        margin-top: 0.8rem;
        font-size: 0.85rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #30363d;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🏥 Hospital AI")

    st.markdown("---")

    st.markdown("### 🤖 Agents")

    st.markdown(
        """
        **🧠 Orchestrator Agent**  
        Routes incoming questions.

        **🗄️ NLP-to-SQL Agent**  
        Queries patient records.

        **📚 RAG Agent**  
        Retrieves hospital policies.
        """
    )

    st.markdown("---")

    st.markdown("### ⚙️ Technology")

    st.markdown(
        """
        - Google Gemini
        - SQLite
        - FAISS
        - Sentence Transformers
        - Streamlit
        """
    )

    st.markdown("---")

    st.info(
        "Patient data is synthetic and used only "
        "for demonstration and educational purposes."
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-header">

        <div class="main-title">
            🏥 Hospital AI Assistant
        </div>

        <div class="subtitle">
            Intelligent multi-agent assistant for patient records
            and hospital policy information.
        </div>

        <div class="status">
            ● AI System Online
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# AGENT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">Multi-Agent Architecture</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="agent-card">

            <div class="agent-icon">🧠</div>

            <div class="agent-title">
                Orchestrator
            </div>

            <div class="agent-description">
                Understands the question and selects
                the appropriate specialist agent.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="agent-card">

            <div class="agent-icon">🗄️</div>

            <div class="agent-title">
                NLP-to-SQL
            </div>

            <div class="agent-description">
                Converts natural language into safe
                read-only SQL queries.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="agent-card">

            <div class="agent-icon">📚</div>

            <div class="agent-title">
                RAG Agent
            </div>

            <div class="agent-description">
                Retrieves relevant information from
                hospital policy documents.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# QUESTION SECTION
# =========================================================

st.markdown(
    '<div class="section-title">Ask Hospital AI</div>',
    unsafe_allow_html=True
)

question = st.text_input(
    "Question",
    placeholder="Example: How many patients have diabetes?",
    label_visibility="collapsed"
)


# =========================================================
# EXAMPLE QUESTIONS
# =========================================================

st.caption("Try an example:")

example_col1, example_col2, example_col3 = st.columns(3)

with example_col1:

    if st.button(
        "🩺 Patients with diabetes",
        use_container_width=True
    ):
        question = "How many patients have diabetes?"


with example_col2:

    if st.button(
        "📊 Average patient age",
        use_container_width=True
    ):
        question = "What is the average age of the patients?"


with example_col3:

    if st.button(
        "📚 Visiting hours",
        use_container_width=True
    ):
        question = "What are the hospital visiting hours?"


# =========================================================
# ASK BUTTON
# =========================================================

ask = st.button(
    "Ask AI  →",
    type="primary",
    use_container_width=True
)


# =========================================================
# PROCESS QUESTION
# =========================================================

if ask:

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    else:

        with st.spinner(
            "🧠 Orchestrator is analyzing your question..."
        ):

            try:

                response = hospital_ai.hospital_assistant(
                    question
                )

                # =================================================
                # RESULT HEADER
                # =================================================

                st.markdown(
                    '<div class="section-title">Response</div>',
                    unsafe_allow_html=True
                )

                # =================================================
                # AGENT
                # =================================================

                agent = response["agent"]

                st.markdown(
                    f"""
                    <div class="agent-badge">
                        🤖 Handled by: <strong>{agent}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # =================================================
                # ANSWER
                # =================================================

                st.markdown(
                    f"""
                    <div class="answer-card">

                        <div class="answer-label">
                            Answer
                        </div>

                        <div class="answer-text">
                            {response["answer"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # =================================================
                # DETAILS
                # =================================================

                with st.expander(
                    "🔍 View technical details"
                ):

                    st.write(
                        "**Route:**",
                        response["route"]
                    )

                    # SQL
                    if response["sql"]:

                        st.markdown(
                            "**Generated SQL:**"
                        )

                        st.code(
                            response["sql"],
                            language="sql"
                        )

                    # Sources
                    if response["sources"]:

                        st.markdown(
                            "**Retrieved Sources:**"
                        )

                        unique_sources = []

                        for source in response["sources"]:

                            filename = source["filename"]

                            if filename not in unique_sources:

                                unique_sources.append(
                                    filename
                                )

                        for filename in unique_sources:

                            st.markdown(
                                f"📄 `{filename}`"
                            )

            except Exception as e:

                st.error(
                    f"An error occurred: {str(e)}"
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        Hospital AI Assistant · Multi-Agent RAG System<br>

        Built with Gemini · SQLite · FAISS · Streamlit

        <br><br>

        ⚠️ Synthetic patient data only — not for real clinical use.

    </div>
    """,
    unsafe_allow_html=True
)
