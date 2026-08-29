# How to Run the RAG Project 🚀

This project implements a Retrieval-Augmented Generation (RAG) system using **Groq** for LLM generation, **HuggingFace** for local embeddings, and **ChromaDB** as the vector store.

## 📋 Prerequisites
- Python 3.11 or higher
- A Groq API Key (Get one for free at [console.groq.com](https://console.groq.com))
- Git installed

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sagarnmore2-datascience/Employee_AI_Project.git
cd Employee_AI_Project
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to avoid dependency conflicts.
```bash
# Create environment
python -m venv venv

# Activate environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example env file
cp .env.example .env
```
Open the `.env` file in a text editor and add your Groq API Key:
```text
GROQ_API_KEY=your_actual_groq_api_key_here
```

---

## 🚀 Running the Project

### 1. Start the API Server
```bash
python app.py
```
The server will start at `http://localhost:8000`.

### 2. Using the API

#### A. Ingest a Document (Upload)
Use this to add a PDF or Text file to the AI's memory.
```bash
curl -X POST "http://localhost:8000/ingest" -F "file=@/path/to/your/document.pdf"
```

#### B. Ask a Question
Ask a question based on the documents you uploaded.
```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are the key findings in the document?"}'
```

---

## 🧪 Learning & Testing
- **Local Embeddings**: The first time you run the project, it will download the `all-MiniLM-L6-v2` model from HuggingFace (approx. 80MB).
- **Vector Store**: Your indexed data is stored locally in the `./chroma_db` folder.
- **Health Check**: Visit `http://localhost:8000/health` in your browser to verify the server is online.

## 🛠️ Troubleshooting
- **API Key Error**: Ensure your `.env` file is in the root directory and the key is correct.
- **Port Already in Use**: If port 8000 is taken, change the port in `app.py` (bottom line) to `port=8080`.
- **ModuleNotFoundError**: Ensure you have activated the virtual environment (`venv`) before running the app.
