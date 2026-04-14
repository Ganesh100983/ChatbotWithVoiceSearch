"""PDF Loading and Document Processing module."""

from pathlib import Path
from typing import List, Optional
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP


class PDFLoader:
    """Handles PDF loading and text extraction."""

    def __init__(self, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP):
        """Initialize PDF loader with text splitting configuration.
        
        Args:
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )

    def load_pdf(self, file_path: str) -> List[Document]:
        """Load a single PDF file.
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            List of documents
        """
        try:
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            print(f"Loaded {len(documents)} pages from {file_path}")
            return documents
        except Exception as e:
            print(f"Error loading PDF {file_path}: {str(e)}")
            return []

    def load_all_pdfs(self, directory: Optional[str] = None) -> List[Document]:
        """Load all PDF files from a directory.
        
        Args:
            directory: Directory path. Defaults to DATA_DIR
            
        Returns:
            List of all documents
        """
        if directory is None:
            directory_path = Path(DATA_DIR)
        else:
            directory_path = Path(directory)
        if not directory_path.exists():
            print(f"Directory {directory_path} does not exist")
            return []

        all_documents = []
        pdf_files = list(directory_path.glob("*.pdf"))
        
        if not pdf_files:
            print(f"No PDF files found in {directory_path}")
            return []

        for pdf_file in pdf_files:
            print(f"Processing {pdf_file.name}...")
            documents = self.load_pdf(str(pdf_file))
            all_documents.extend(documents)

        return all_documents

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks.
        
        Args:
            documents: List of documents to split
            
        Returns:
            List of chunked documents
        """
        split_docs = self.text_splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(split_docs)} chunks")
        return split_docs

    def process_pdfs(self, directory: Optional[str] = None) -> List[Document]:
        """Complete pipeline: load and split PDFs.
        
        Args:
            directory: Directory containing PDFs
            
        Returns:
            List of processed document chunks
        """
        documents = self.load_all_pdfs(directory)
        if not documents:
            return []
        return self.split_documents(documents)
