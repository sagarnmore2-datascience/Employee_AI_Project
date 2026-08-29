import os
from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class RAGRetriever:
    """Handles searching and retrieving relevant documents from ChromaDB."""

    def __init__(self, persist_directory: str = "./chroma_db"):
        self.persist_directory = persist_directory
        # Use the same HuggingFace model used in ingestion
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectorstore = self._load_vectorstore()

    def _load_vectorstore(self):
        """Connects to the existing ChromaDB store."""
        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )

    def retrieve_relevant_chunks(self, query: str, k: int = 3) -> List:
        """Performs similarity search to find the top-k most relevant chunks."""
        return self.vectorstore.similarity_search(query, k=k)

    def clear_database(self):
        """Deletes the local ChromaDB directory to start fresh."""
        import shutil
        if os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
            self.vectorstore = None
            print(f"Database at {self.persist_directory} cleared.")
        else:
            print("No database found to clear.")

if __name__ == "__main__":
    retriever = RAGRetriever()
    print("Retriever initialized with HuggingFace embeddings. Ready to search.")
