# Asylum Seekers Assistant

An AI-powered assistant that helps asylum seekers understand the Dublin Regulation using Retrieval-Augmented Generation (RAG).

The application retrieves information from official Dublin Regulation documents and generates simple, clear answers using a Large Language Model (LLM), while providing the source pages used to answer each question.

---

## Overview

Understanding asylum procedures can be difficult due to complex legal language and regulations.

**Asylum Seekers Assistant** uses Artificial Intelligence and document retrieval techniques to help users find relevant information from official asylum-related documents.

The system is designed to:

- Answer questions about the Dublin Regulation
- Use only information from the provided documents
- Provide transparent sources for generated answers
- Explain information using simple English

---

# Features

## 🤖 AI Question Answering

Users can ask questions about asylum procedures and receive answers generated using OpenAI's GPT model.

Example questions:

- "How long does the Dublin process take?"
- "Can I be transferred to another country?"
- "Which country is responsible for my asylum application?"

---

## 📚 Retrieval-Augmented Generation (RAG)

The application does not rely only on the language model.

Instead, it:

1. Searches relevant document sections.
2. Retrieves the most relevant information.
3. Provides this context to the AI model.
4. Generates an answer based only on the retrieved documents.

This reduces hallucination and keeps answers grounded in official information.

---

## 🔎 Source References

Each answer includes the document pages used to generate the response.

Example:

```
Answer:
The transfer process usually takes up to 6 months.

Sources:
Page 9
Page 11
```

---

# Architecture

```
                 User
                  |
                  |
                  v
          Streamlit Interface
                  |
                  |
                  v
            User Question
                  |
                  |
                  v
          Semantic Search
                  |
                  |
                  v
             ChromaDB
                  |
                  |
        Relevant Document Chunks
                  |
                  |
                  v
          GPT-4.1-mini LLM
                  |
                  |
                  v
              Final Answer
```

---

# Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python 3.13 |
| Frontend | Streamlit |
| AI Framework | LangChain |
| Large Language Model | OpenAI GPT-4.1-mini |
| Vector Database | ChromaDB |
| Embeddings | BAAI/bge-small-en-v1.5 |
| Embedding Framework | Hugging Face Sentence Transformers |
| Document Processing | PyPDF |
| Environment Management | Python dotenv |
| Containerization | Docker |

---

# Project Structure

```
Asylum-seekers-assistant/

│
├── app.py                  # Streamlit user interface
│
├── rag.py                  # Retrieval-Augmented Generation pipeline
│
├── requirements.txt        # Python dependencies
│
├── Dockerfile              # Docker image configuration
│
├── docker-compose.yml      # Container orchestration
│
├── .dockerignore
│
├── .env                    # Environment variables
│
├── data/
│   └── documents           # Source documents
│
├── chroma_db/              # Vector database
│
└── README.md
```

---

# Installation (Local Development)

## Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/Asylum-seekers-assistant.git

cd Asylum-seekers-assistant
```

---

## Create virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

## Configure environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run application

```powershell
python -m streamlit run app.py
```

Application available at:

```
http://localhost:8501
```

---

# Docker Deployment

## Build Docker image

```bash
docker compose build
```

## Start application

```bash
docker compose up
```

Application available at:

```
http://localhost:8501
```

Docker provides:

- Isolated Python environment
- Reproducible dependencies
- Consistent deployment across machines

---

# How It Works

## 1. Document Processing

The source documents are loaded and processed.

Documents are:

- Extracted from PDF files
- Split into smaller chunks
- Converted into numerical embeddings

---

## 2. Vector Storage

The embeddings are stored inside ChromaDB.

This allows semantic searching instead of simple keyword matching.

---

## 3. User Query

When a user asks a question:

```
User Question
        |
        v
Embedding Generation
        |
        v
Similarity Search
        |
        v
Relevant Documents
```

---

## 4. Answer Generation

The retrieved information is sent to GPT-4.1-mini.

The model generates an answer using only the provided context.

---

# Example

Question:

```
How long does the Dublin transfer process take?
```

Answer:

```
The process of deciding which country will examine your asylum application and transferring you to that country usually takes up to 6 months.

Sources:
Page 9
Page 11
```

---

# Future Improvements

Possible future improvements:

- 🌍 Multilingual support
- 💬 Conversation memory
- 📄 Multiple document support
- 🔍 Highlight relevant document passages
- ☁️ Cloud deployment
- 🐳 Improved Docker deployment
- 🔐 User authentication

---

# Disclaimer

This application provides information from uploaded documents and is not legal advice.

Users should contact official authorities or qualified legal professionals for advice about their individual situation.

---

# Author

Created by Yohana

