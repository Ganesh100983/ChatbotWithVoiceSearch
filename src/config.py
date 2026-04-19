"""Configuration module for RAG Chatbot."""


import os
import warnings
from pathlib import Path
from dotenv import load_dotenv

# Suppress all warnings globally (including HuggingFace and deprecation warnings)
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
VECTOR_STORE_PATH = PROJECT_ROOT / "faiss_index"

# API Configuration

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-5-nano")

# Vector Store Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)
VECTOR_STORE_PATH.mkdir(exist_ok=True)


def validate_config():
    """Validate essential configuration."""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")
    return True
