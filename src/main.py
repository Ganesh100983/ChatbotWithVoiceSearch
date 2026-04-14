"""Main entry point for RAG Chatbot."""

import sys
from pathlib import Path
from src.config import validate_config, DATA_DIR, VECTOR_STORE_PATH
from src.pdf_loader import PDFLoader
from src.vector_store import FAISSVectorStore
from src.chatbot import RAGChatbot


def initialize_vector_store():
    """Initialize or load vector store.
    
    Returns:
        FAISSVectorStore instance
    """
    vector_store = FAISSVectorStore()

    # Check if vector store already exists
    if vector_store.exists():
        print("Vector store found. Loading...")
        vector_store.load_vector_store()
        return vector_store

    # Create new vector store from PDFs
    print("Vector store not found. Creating from PDF files...")

    pdf_loader = PDFLoader()
    documents = pdf_loader.process_pdfs(str(DATA_DIR))

    if not documents:
        print("Error: No PDF documents found. Please add PDF files to the 'data' folder.")
        sys.exit(1)

    vector_store.create_vector_store(documents)
    vector_store.save_vector_store()

    return vector_store


def main():
    """Main function to run the chatbot."""
    try:
        # Validate configuration
        validate_config()

        print("\n" + "="*60)
        print("RAG Chatbot Initialization")
        print("="*60 + "\n")

        # Initialize vector store
        vector_store = initialize_vector_store()

        # Create chatbot instance
        chatbot = RAGChatbot(vector_store)

        # Start interactive chat
        chatbot.chat()

    except ValueError as e:
        print(f"Configuration Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
