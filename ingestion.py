from typing import List
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class RAGIngestor:
    """Handles the loading, chunking, and indexing of documents into ChromaDB."""

    def __init__(self, persist_directory: str = "./chroma_db"):
        self.persist_directory = persist_directory
        # Initialize HuggingFace Embeddings (all-MiniLM-L6-v2)
        # This will download the model locally on the first run
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def load_document(self, file_path: str):
        """Loads a file based on its extension."""
        if file_path.endswith('.pdf'):
            loader = PyPDFLoader(file_path)
        elif file_path.endswith('.txt'):
            loader = TextLoader(file_path)
        else:
            raise ValueError("Unsupported file format. Please use .pdf or .txt")

        return loader.load()

    def chunk_documents(self, documents, chunk_size: int = 1000, chunk_overlap: int = 100):
        """Splits long documents into smaller, overlapping chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            add_start_index=True,
        )
        return text_splitter.split_documents(documents)

    def index_documents(self, chunks: List):
        """Stores chunks in the ChromaDB vector database."""
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        return vectorstore

if __name__ == "__main__":
    ingestor = RAGIngestor()
    print("Ingestor initialized with HuggingFace embeddings. Ready to process documents.")
