from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List

from ingestion import RAGIngestor
from retrieval import RAGRetriever
from generation import RAGGenerator

app = FastAPI(title="Learning RAG API")

# Initialize our RAG components
ingestor = RAGIngestor()
retriever = RAGRetriever()
generator = RAGGenerator()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    sources: List[str]

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "RAG System is online"}

@app.post("/ingest")
async def ingest_file(file: UploadFile = File(...)):
    """Uploads a file and adds it to the vector database."""
    try:
        # Save uploaded file locally temporarily
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # 1. Load
        docs = ingestor.load_document(file_path)
        # 2. Chunk
        chunks = ingestor.chunk_documents(docs)
        # 3. Index
        ingestor.index_documents(chunks)

        # Clean up temp file
        import os
        os.remove(file_path)

        return {"message": f"Successfully indexed {file.filename} into the database."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """Asks a question based on the indexed documents."""
    try:
        # 1. Retrieve
        relevant_chunks = retriever.retrieve_relevant_chunks(request.question)

        if not relevant_chunks:
            return AnswerResponse(answer="No relevant information found in the database.", sources=[])

        # 2. Generate
        answer = generator.generate_answer(request.question, relevant_chunks)

        # 3. Extract sources (page content)
        sources = [doc.page_content for doc in relevant_chunks]

        return AnswerResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
