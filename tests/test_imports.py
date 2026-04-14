"""Tests for RAG Chatbot modules."""

import pytest
from pathlib import Path


@pytest.fixture
def sample_text():
    """Fixture for sample test text."""
    return "This is a test document about Python programming."


def test_config_imports():
    """Test that config module imports successfully."""
    from src.config import validate_config
    assert callable(validate_config)


def test_pdf_loader_imports():
    """Test that pdf_loader module imports successfully."""
    from src.pdf_loader import PDFLoader
    assert callable(PDFLoader)


def test_vector_store_imports():
    """Test that vector_store module imports successfully."""
    from src.vector_store import FAISSVectorStore
    assert callable(FAISSVectorStore)


def test_chatbot_imports():
    """Test that chatbot module imports successfully."""
    from src.chatbot import RAGChatbot
    assert callable(RAGChatbot)
