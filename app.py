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

st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ================= HEADER ================= */

.main-header {
    background: linear-gradient(
        135deg,
        #151a23,
        #1d2633
    );

    border: 1px solid #2d3745;
    border-radius: 20px;

    padding: 35px;

    margin-bottom: 35px;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #ffffff;
}

.subtitle {
    font-size: 17px;
    color: #aeb7c4;
    margin-top: 10px;
}

.status {
    display: inline-block;

    margin-top: 20px;

    padding: 8px 15px;

    border-radius: 20px;

    background-color: #123c2a;

    color: #4ade80;

    font-size: 14px;

    font-weight: 600;
}


/* ================= SECTION ================= */

.section-title {
    font-size: 26px;
    font-weight: 700;
    color: #ffffff;

    margin-top: 30px;
    margin-bottom: 18px;
}


/* ================= AGENT CARDS ================= */

.agent-card {
    background-color: #151a23;

    border: 1px solid #2d3745;

    border-radius: 16px;

    padding: 25px;

    min-height: 190px;
}

.agent-icon {
    font-size: 34px;
    margin-bottom: 12px;
}

.agent-title {
    font-size: 21px;
    font-weight: 700;
    color: #ffffff;

    margin-bottom: 10px;
}

.agent-description {
    font-size: 14px;
    line-height: 1.6;

    color: #aeb7c4;
}


/* ================= RESULT ================= */

.result-box {
    background-color: #151a23;

    border: 1px solid #2d3745;

    border-radius: 16px;

    padding: 25px;

    margin-top: 25px;
}

.result-label {
    font-size: 13px;

    color: #8b98a9;

    font-weight: 600;

    margin-bottom: 8px;
}

.result-answer {
    font-size: 21px;

    color: #ffffff;

    line-height: 1.6;
}


/* ================= AGENT BADGE ================= */

.agent-badge {
    display: inline-block;

    background-color: #123c2a;

    color: #4ade80;

    padding: 8px 15px;

    border-radius: 20px;

    font-size: 14px;

    font-weight: 600;

    margin-top: 20px;
}


/* ================= SIDEBAR ================= */

[data-testid="stSidebar"] {
    background-color: #11151c;
}

.sidebar-title {
    font-size: 23px;

    font-weight: 700;

    color: #ffffff;

    margin-bottom: 20px;
}

.sidebar-item {
    color: #c4ccd6;

    padding: 8px 0;

    font-size: 15px;
}

.sidebar-info {
    background-color: #182b44;

    color: #9ec5ff;

    padding: 15px;

    border-radius: 12px;

    margin-top: 25px;

    font-size: 13px;

    line-height: 1.5;
}


/* ================= FOOTER ================= */

.footer {
    text-align: center;

    color: #6f7b8a;

    font-size: 13px;

    margin-top: 50px;

    padding-top: 20px;

    border-top: 1px solid #252c36;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">
        🏥 Hospital AI
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<h4>🤖 Multi-Agent Architecture</h4>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="sidebar-item">🧠 Orchestrator Agent</div>
    <div class="sidebar-item">🗄️ NLP-to-SQL Agent</div>
    <div class="sidebar-item">📚 RAG Agent</div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown(
        "<h4>⚙️ System</h4>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="sidebar-item">🟢 AI System Online</div>
    <div class="sidebar-item">🗃️ SQLite Database</div>
    <div class="sidebar-item">🔎 FAISS Retrieval</div>
    <div class="sidebar-item">✨ Gemini AI</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-info">
        Patient data is synthetic and used only
        for demonstration purposes.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.html("""
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
""")


# =========================================================
# MULTI-AGENT ARCHITECTURE
# =========================================================

st.html("""
<div class="section-title">
    🤖 Multi-Agent Architecture
</div>
""")


col1, col2, col3 = st.columns(3)


# =========================================================
# ORCHESTRATOR
# =========================================================

with col1:

    st.html("""
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
    """)


# =========================================================
# NLP TO SQL
# =========================================================

with col2:

    st.html("""
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
    """)


# =========================================================
# RAG
# =========================================================

with col3:

    st.html("""
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
    """)


# =========================================================
# QUESTION SECTION
# =========================================================

st.html("""
<div class="section-title">
    💬 Ask the Hospital AI
</div>
""")


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
            "Please enter a question."
        )

    else:

        with st.spinner(
            "🤖 Processing your question..."
        ):

            try:

                response = hospital_ai.hospital_assistant(
                    question
                )


                # =============================================
                # SELECTED AGENT
                # =============================================

                st.html(f"""
                <div class="agent-badge">
                    ✓ Selected Agent: {response["agent"]}
                </div>
                """)


                # =============================================
                # ANSWER
                # =============================================

                st.html(f"""
                <div class="result-box">

                    <div class="result-label">
                        AI RESPONSE
                    </div>

                    <div class="result-answer">
                        {response["answer"]}
                    </div>

                </div>
                """)


                # =============================================
                # ROUTING DETAILS
                # =============================================

                with st.expander(
                    "🔍 View routing details"
                ):

                    st.write(
                        "**Route:**",
                        response["route"]
                    )


                    # =========================================
                    # SQL
                    # =========================================

                    if response.get("sql"):

                        st.write(
                            "**Generated SQL:**"
                        )

                        st.code(
                            response["sql"],
                            language="sql"
                        )


                    # =========================================
                    # RAG SOURCES
                    # =========================================

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

st.html("""
<div class="section-title">
    💡 Example Questions
</div>
""")


example1, example2, example3 = st.columns(3)


with example1:

    st.info(
        "🩺 **Patient Data**\n\n"
        "How many patients have diabetes?"
    )


with example2:

    st.info(
        "🏥 **Hospital Policy**\n\n"
        "What are the hospital visiting hours?"
    )


with example3:

    st.info(
        "💰 **Database Query**\n\n"
        "What is the average billing amount?"
    )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">
    🏥 Hospital AI Assistant
    &nbsp; • &nbsp;
    Multi-Agent AI System
    &nbsp; • &nbsp;
    Synthetic Data for Demonstration
</div>
""")
