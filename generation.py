import os
from typing import List
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class RAGGenerator:
    """Handles the final step: generating an answer using Groq LLM and retrieved context."""

    def __init__(self, model_name: str = "llama3-8b-8192"):
        # Initialize the Groq LLM
        # It uses GROQ_API_KEY from the environment
        self.llm = ChatGroq(model=model_name, temperature=0)

    def generate_answer(self, query: str, context_chunks: List) -> str:
        """
        Uses a prompt template to generate an answer based on the provided context.
        """
        # 1. Combine the retrieved chunks into a single context string
        context_text = "\n\n".join([doc.page_content for doc in context_chunks])

        # 2. Create a system prompt to ensure the AI only uses the provided context
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", (
                "You are a helpful AI assistant. Use the provided context to answer the user's question. "
                "If the answer is not contained within the context, honestly state that you do not have "
                "enough information to answer. Do not make up information.\n\n"
                "Context:\n{context}"
            )),
            ("user", "{question}"),
        ])

        # 3. Create the chain
        chain = prompt_template | self.llm

        # 4. Run the chain
        response = chain.invoke({
            "context": context_text,
            "question": query
        })

        return response.content

if __name__ == "__main__":
    generator = RAGGenerator()
    print("Generator initialized with Groq LLM. Ready to produce answers.")
