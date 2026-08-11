
# 🏥 Hospital AI Assistant

An AI-powered multi-agent application that allows hospital staff to query synthetic patient records and hospital policy documents using plain English.

## 🚀 Project Overview

The system uses an Orchestrator Agent to classify incoming questions and automatically route them to the appropriate specialized agent.

- **NLP-to-SQL Agent** → answers questions about structured patient data.
- **RAG Agent** → retrieves information from hospital policy documents.
- **Orchestrator Agent** → decides which agent should handle each question.

The application provides a single conversational interface through Streamlit.

🚀 Live Demo  https://hospitalaimultiagentsystem-i8mypdaew5njj8h6thhwcs.streamlit.app/

## 🏗️ Architecture
```text


                    User
                     |
                     v
             Orchestrator Agent
                /           \
               /             \
              v               v
      NLP-to-SQL Agent     RAG Agent
              |               |
              v               v
           SQLite           FAISS
              |               |
              v               v
       Patient Records    Policy Documents
               \             /
                \           /
                 v         v
                  Gemini
                     |
                     v
                Final Answer

```

🚀 Live Demo  https://hospitalaimultiagentsystem-i8mypdaew5njj8h6thhwcs.streamlit.app/

## 📸 Project Screenshots

### NLP-to-SQL Agent

![NLP-to-SQL Agent](./screenshots/01_sql_agent.png)

### Database Query

![Database Query](./screenshots/02_database_result.png)

### RAG Agent

![RAG Agent](./screenshots/03_rag_agent.png)

### Out-of-Scope Query

![Out-of-Scope Query](./screenshots/04_out_of_scope.png)
