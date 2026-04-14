# Quick Start Guide - RAG Chatbot with Streamlit UI

## ⚡ Getting Started (5 minutes)

### 1. Clone or Open the Project
```bash
cd d:\pythonwork\RAG_Chatbot
```

### 2. Set Up Environment Variables
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your_api_key_here
LLM_MODEL=gpt-3.5-turbo
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

### 3. Add PDF Files
Place your PDF documents in the `data/` folder:
```
data/
├── document1.pdf
├── document2.pdf
└── document3.pdf
```

### 4. Install Dependencies (Already Done)
Dependencies have been installed via UV. You can verify by running:
```bash
uv sync
```

### 5. Run the Streamlit UI
```bash
uv run streamlit run streamlit_app.py
```

The app will open in your browser at: **http://localhost:8501**

## 🎨 Streamlit UI Features

### Main Interface
- **Chat Input**: Ask questions about your documents
- **Chat History**: View all previous conversations
- **Source Citations**: See which documents provided the answer

### Sidebar Features
- **Load/Create Vector Store**: Initialize or load the FAISS index
- **Vector Store Status**: Check if the index is ready
- **Clear Chat History**: Reset the conversation
- **Settings**: View configuration details
- **Help**: Built-in documentation

### First Run
1. Click **"Load/Create Vector Store"** button
2. The app will read PDFs from the `data/` folder
3. It will create a FAISS index (stored in `faiss_index/`)
4. Start asking questions!

## 🔄 Alternative: CLI Mode

If you prefer terminal-based interaction:
```bash
uv run python -m src.main
```

## 📁 Project Structure

```
RAG_Chatbot/
├── src/
│   ├── config.py           # Configuration management
│   ├── pdf_loader.py       # PDF loading
│   ├── vector_store.py     # FAISS management
│   ├── chatbot.py          # RAG logic
│   └── main.py             # CLI entry point
├── streamlit_app.py        # Streamlit UI (use this!)
├── data/                   # Add your PDFs here
├── pyproject.toml          # Dependencies
└── .env                    # Your API keys
```

## 🐛 Troubleshooting

### Error: "OPENAI_API_KEY is not set"
- Make sure you created `.env` file
- Add your actual API key (starts with `sk-`)

### Error: "No PDF documents found"
- Make sure PDF files are in the `data/` folder
- Check file permissions

### Error: "Vector store not found"
- Click the "Load/Create Vector Store" button in the sidebar
- It will automatically process your PDFs

### Streamlit app won't start
```bash
# Try reinstalling Streamlit
uv pip install --upgrade streamlit
```

## 💡 Example Workflow

1. **Add a PDF**: Place a PDF about Python in `data/`
2. **Load Store**: Click "Load/Create Vector Store"
3. **Ask Question**: Type "What is Python?"
4. **Get Answer**: Bot responds with relevant sections
5. **View Sources**: Click "View Sources" to see which pages helped

## 📚 Example Questions

- "What is the main topic of this document?"
- "Summarize the key points"
- "What are the requirements mentioned?"
- "Explain the technical specifications"
- "What are the costs and pricing?"

## 🚀 Next Steps

- Add more PDFs for a richer knowledge base
- Adjust `CHUNK_SIZE` and `CHUNK_OVERLAP` for different document types
- Try different LLM models (GPT-4, Claude, etc.)
- Customize the prompt template in `src/chatbot.py`

## 🆘 Need Help?

Check the README.md for:
- Detailed configuration options
- Development setup
- Testing instructions
- Advanced features

---

**Enjoy your RAG Chatbot! 🤖**
