<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cfa72f7a-303d-4774-8965-07faf3f79140" />
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
```text<img width="1205" height="504" alt="Screenshot 2026-08-11 163343" src="https://github.com/user-attachments/assets/956f1932-1f5e-4737-bcbf-8c5164db0b92" />
<img width="790" height="350" alt="Screenshot 2026-08-11 163129" src="https://github.com/user-attachments/assets/8f741ce7-91cc-45ba-9571-1eb144e8c053" />
<img width="1902" height="970" alt="Screenshot 2026-08-11 162109" src="https://github.com/user-attachments/assets/5f177033-f26f-40e4-ba31-8080335830b2" />
<img width="1917" height="961" alt="Screenshot 2026-08-11 162023" src="https://github.com/user-attachments/assets/e9756997-b8ca-41ce-a935-c027fac2c88f" />


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


