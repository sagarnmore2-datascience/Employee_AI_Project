# Specification: Learning RAG Project

## 1. Project Overview
The goal of this project is to implement a **Retrieval-Augmented Generation (RAG)** system. The system will allow a user to upload a document, index its content into a vector database, and ask questions based specifically on that document.

This project is built for **learning purposes**, focusing on a modular architecture that separates data ingestion, retrieval, and generation.

## 2. Architecture Flow
`Document` $\rightarrow$ `Text Splitter` $\rightarrow$ `Embedding Model` $\rightarrow$ `Vector Database` $\rightarrow$ `Similarity Search` $\rightarrow$ `LLM Prompt` $\rightarrow$ `Final Answer`

## 3. Tech Stack
- **Language**: Python 3.11
- **Orchestration**: LangChain (Industry standard for RAG)
- **LLM**: groq
- **Vector Database**: ChromaDB (Local, open-source)
- **Embeddings**: HuggingFace `all-MiniLM-L6-v2` (Local/Free)
- **API Framework**: FastAPI
- **CI/CD**: GitHub Actions & Docker

## 4. Functional Requirements

### Module A: Ingestion Pipeline
- [ ] Support for `.txt` and `.pdf` files.
- [ ] Recursive character splitting (chunking) to maintain context.
- [ ] Vectorization of chunks using an embedding model.
- [ ] Persistent storage in ChromaDB.

### Module B: Retrieval Pipeline
- [ ] Conversion of user queries into vectors.
- [ ] Top-K similarity search (retrieve top 3-5 relevant chunks).
- [ ] Ability to clear the database to start fresh.

### Module C: Generation Pipeline
- [ ] Implementation of a "System Prompt" to prevent hallucinations.
- [ ] Context-injection: Feeding retrieved chunks into the LLM prompt.
- [ ] Generation of a natural language response based on the context.

### Module D: API Layer
- [ ] `POST /ingest`: Upload a file and index it.
- [ ] `POST /ask`: Send a question and receive an answer.
- [ ] `GET /health`: Check system status.

## 5. Success Metrics (Definition of Done)
- [ ] The system can answer a question using a specific fact found in the uploaded document.
- [ ] The system refuses to answer (or states it doesn't know) if the information is not in the document.
- [ ] The CI/CD pipeline passes all tests on every push to `master`.
