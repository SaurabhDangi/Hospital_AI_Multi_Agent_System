
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



## 📸 Project Screenshots

### 1. NLP-to-SQL Agent
<img width="1900" height="796" alt="Screenshot 2026-08-11 141700" src="https://github.com/user-attachments/assets/54d72601-b400-4da6-90f4-465e29ae0da1" />


### 2. Database Query Result
<img width="1217" height="743" alt="Screenshot 2026-08-11 141937" src="https://github.com/user-attachments/assets/bef1d2b1-4bbe-4a2f-a885-660fec7d8f7e" />

### 3. RAG Agent
<img width="1917" height="961" alt="Screenshot 2026-08-11 162023" src="https://github.com/user-attachments/assets/61cdd598-d5ad-43d2-82c5-0a8683293535" />


### 4. Out-of-Scope Query Handling
<img width="1902" height="970" alt="Screenshot 2026-08-11 162109" src="https://github.com/user-attachments/assets/085e93a2-a284-4d3b-ba50-8c0b6ff26833" />
