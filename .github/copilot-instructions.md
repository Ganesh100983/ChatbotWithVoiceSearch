# RAG Chatbot Project Setup

This is a Retrieval Augmented Generation (RAG) based chatbot using LangChain and FAISS vector database.

## Project Structure
- `src/` - Main source code
- `data/` - PDF files for ingestion
- `pyproject.toml` - UV package configuration

## Key Technologies
- Python 3.11
- LangChain
- FAISS Vector Database
- OpenAI LLM

## Getting Started
1. Install UV package manager
2. Run `uv sync` to install dependencies
3. Set up `.env` file with OpenAI API key
4. Place PDF files in the `data/` folder
5. Run the chatbot application

## Development
- Use `uv run` to execute scripts
- Use `uv run pytest` to run tests
