
import streamlit as st
import hospital_ai


st.set_page_config(
    page_title="Hospital AI Assistant",
    page_icon="🏥",
    layout="centered"
)


# ==============================
# HEADER
# ==============================

st.title("🏥 Hospital AI Assistant")

st.write(
    "Ask questions about patient records "
    "or hospital policies using plain English."
)


# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.header("System Information")

    st.write("🤖 Multi-Agent Architecture")

    st.write("Agents:")
    st.write("• Orchestrator Agent")
    st.write("• NLP-to-SQL Agent")
    st.write("• RAG Agent")

    st.info(
        "Patient data is synthetic and used "
        "only for demonstration."
    )


# ==============================
# QUESTION INPUT
# ==============================

question = st.text_input(
    "Ask your question:",
    placeholder="Example: How many patients have diabetes?"
)


# ==============================
# ASK BUTTON
# ==============================

if st.button("Ask", type="primary"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Processing your question..."):

            try:

                response = hospital_ai.hospital_assistant(
                    question
                )

                # ==============================
                # AGENT
                # ==============================

                st.success(
                    f"Selected Agent: {response['agent']}"
                )

                # ==============================
                # ANSWER
                # ==============================

                st.subheader("Answer")

                st.write(
                    response["answer"]
                )

                # ==============================
                # ROUTING DETAILS
                # ==============================

                with st.expander(
                    "View routing details"
                ):

                    st.write(
                        "Route:",
                        response["route"]
                    )

                    # SQL information
                    if response["sql"]:

                        st.write(
                            "Generated SQL:"
                        )

                        st.code(
                            response["sql"],
                            language="sql"
                        )

                    # RAG sources
                    if response["sources"]:

                        st.write("Sources:")

                        unique_sources = []

                        for source in response["sources"]:

                            filename = source["filename"]

                            if filename not in unique_sources:

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
