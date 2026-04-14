"""FAISS Vector Store Management module."""

import os
from typing import List, Optional, Dict, Any
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from src.config import VECTOR_STORE_PATH


class FAISSVectorStore:
    """Manages FAISS vector store for document retrieval."""

    def __init__(self, index_name: str = "documents"):
        """Initialize FAISS vector store.
        
        Args:
            index_name: Name of the vector store index
        """
        self.index_name = index_name
        self.index_path = VECTOR_STORE_PATH / index_name
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_store: Optional[FAISS] = None

    def create_vector_store(self, documents: List[Document]) -> FAISS:
        """Create a new FAISS vector store from documents.
        
        Args:
            documents: List of documents to embed and store
            
        Returns:
            FAISS vector store instance
        """
        print(f"Creating FAISS vector store with {len(documents)} documents...")
        self.vector_store = FAISS.from_documents(
            documents,
            self.embeddings,
        )
        print("Vector store created successfully")
        return self.vector_store

    def save_vector_store(self) -> None:
        """Save the vector store to disk."""
        if self.vector_store is None:
            raise ValueError("Vector store not initialized. Create one first.")
        
        print(f"Saving vector store to {self.index_path}...")
        self.vector_store.save_local(str(self.index_path))
        print("Vector store saved successfully")

    def load_vector_store(self) -> FAISS:
        """Load vector store from disk.
        
        Returns:
            Loaded FAISS vector store
        """
        if not self.index_path.exists():
            raise FileNotFoundError(f"Vector store not found at {self.index_path}")
        
        print(f"Loading vector store from {self.index_path}...")
        self.vector_store = FAISS.load_local(
            str(self.index_path),
            self.embeddings,
            allow_dangerous_deserialization=True
        )
        print("Vector store loaded successfully")
        return self.vector_store

    def add_documents(self, documents: List[Document]) -> None:
        """Add more documents to existing vector store.
        
        Args:
            documents: Documents to add
        """
        if self.vector_store is None:
            raise ValueError("Vector store not initialized")
        
        print(f"Adding {len(documents)} documents to vector store...")
        self.vector_store.add_documents(documents)
        print("Documents added successfully")

    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """Search for similar documents.
        
        Args:
            query: Search query
            k: Number of results to return
            
        Returns:
            List of similar documents
        """
        if self.vector_store is None:
            raise ValueError("Vector store not initialized")
        
        return self.vector_store.similarity_search(query, k=k)

    def as_retriever(self, search_kwargs: Optional[Dict[str, Any]] = None):
        """Convert vector store to a retriever.
        
        Args:
            search_kwargs: Search parameters
            
        Returns:
            Retriever object for use in chains
        """
        if self.vector_store is None:
            raise ValueError("Vector store not initialized")
        
        if search_kwargs is None:
            search_kwargs = {"k": 4}
        
        return self.vector_store.as_retriever(search_type="similarity", search_kwargs=search_kwargs)

    def is_initialized(self) -> bool:
        """Check if vector store is loaded.
        
        Returns:
            True if vector store is ready
        """
        return self.vector_store is not None

    def exists(self) -> bool:
        """Check if vector store exists on disk.
        
        Returns:
            True if vector store files exist
        """
        return self.index_path.exists()
