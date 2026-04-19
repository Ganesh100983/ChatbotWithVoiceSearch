# 🤖 RAG Chatbot with Voice Features

A sophisticated Retrieval Augmented Generation (RAG) chatbot built with LangChain, FAISS, and OpenAI, featuring advanced voice input and text-to-speech capabilities.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-blue.svg)](https://openai.com)

## ✨ Features

### Core RAG Functionality
- **📄 PDF Processing**: Intelligent document loading and text chunking
- **🔍 Vector Search**: FAISS-powered semantic similarity search
- **🧠 LLM Integration**: Powered by Groq's ultra-fast inference models
- **🧠 LLM Integration**: Powered by OpenAI's GPT models (gpt-3.5-turbo, gpt-4, etc.)
- **📚 Source Citations**: Transparent answer sourcing with page references
- **💾 Persistent Storage**: Automatic vector store saving/loading

### 🎤 Advanced Voice Features
- **🎙️ Voice Input**: Speak questions naturally using microphone
- **🔊 Text-to-Speech**: Bot responses spoken aloud automatically
- **🎯 Real-time Recognition**: Continuous speech processing with noise filtering
- **🎛️ Voice Controls**: Granular settings for voice input/output
- **🧪 Voice Testing**: Built-in TTS testing and microphone validation

### 🎨 Modern Web Interface
- **🌐 Streamlit UI**: Beautiful, responsive web interface
- **📱 Mobile Friendly**: Works on desktop and mobile devices
- **⚡ Real-time Updates**: Live chat with instant responses
- **🎨 Custom Styling**: Professional UI with dark/light themes
- **📊 Status Indicators**: Visual feedback for all operations

## 🚀 Quick Start

### Prerequisites
- **Python 3.11+**
- **UV package manager**
- **OpenAI API key** (get at [platform.openai.com](https://platform.openai.com))
- **Microphone** (for voice input)
- **Speakers/Headphones** (for text-to-speech)

### Installation

1. **Install UV Package Manager**
   ```bash
   # Windows (PowerShell)
   powershell -Command "irm https://astral.sh/uv/install.ps1 | iex"

   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone & Install Dependencies**
   ```bash
   git clone <repository-url>
   cd rag-chatbot
   uv sync
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your Groq API key:
   ```bash
   GROQ_API_KEY=gsk_your_api_key_here
   LLM_MODEL=llama3-70b-8192
    Edit `.env` with your OpenAI API key:
   CHUNK_OVERLAP=200
    OPENAI_API_KEY=sk-your_api_key_here

4. **Optional: Enhanced Voice Support**
   ```bash
   pip install pyaudio  # Better microphone support on Windows
   ```

### Running the Application

```bash
# Launch the web interface
uv run streamlit run src/streamlit_app.py
```

**Access at:** http://localhost:8501

## 🎯 Usage Guide

### Basic Chatbot Usage

1. **Add PDF Documents**
   - Place PDF files in the `data/` folder
   - Click "🔄 Load/Create Vector Store" in the sidebar

2. **Ask Questions**
   - Type questions in the chat input
   - View source citations by expanding "📄 View Sources"
   - Clear history with "🗑️ Clear Chat History"

### 🎤 Voice Features

1. **Enable Voice Features**
   - ✅ **Enable Voice Input**: Allow microphone input
   - ✅ **Enable Text-to-Speech**: Bot speaks responses

2. **Using Voice Input**
   - Click "🎤 Start Voice Listening"
   - Speak clearly into your microphone
   - Voice messages appear with 🎤 prefix
   - Say "stop listening" to end voice input

3. **Voice Commands**
   - **"Stop listening"** - End voice input
   - **"Clear history"** - Reset chat
   - **Test TTS** - Click speaker button to test audio

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GROQ_API_KEY` | Your Groq API key | - | ✅ Yes |
| `LLM_MODEL` | Groq model selection | `llama3-70b-8192` | ❌ No |
| `CHUNK_SIZE` | Document chunk size | `1000` | ❌ No |
| `CHUNK_OVERLAP` | Chunk overlap tokens | `200` | ❌ No |
| `OPENAI_API_KEY` | Your OpenAI API key | - | ✅ Yes |
### Available Groq Models

| Model | Context | Speed | Best For |
|-------|---------|-------|----------|
| `llama3-70b-8192` | 8K | Fast | **General RAG** ⭐ |
| `llama3.1-70b-versatile` | 128K | Medium | **Complex reasoning** |
| `llama3.1-8b-instant` | 128K | Very Fast | **Quick responses** |
| `llama3-8b-8192` | 8K | Fast | **Lightweight** |
| `llama3.1-405b-instruct` | 128K | Slow | **Maximum accuracy** |

## 🏗️ Project Architecture

```
rag-chatbot/
├── 📁 src/
│   ├── config.py           # 🔧 Configuration & environment management
│   ├── chatbot.py          # 🤖 RAG chatbot with Groq integration
│   ├── vector_store.py     # 🗃️ FAISS vector database operations
│   ├── pdf_loader.py       # 📄 PDF processing & text chunking
│   ├── streamlit_app.py    # 🌐 Web interface with voice features
│   ├── voice_handler.py    # 🎤 Speech-to-text & text-to-speech
│   └── main.py            # 💻 CLI interface
├── 📁 data/               # 📚 PDF document storage
├── 📁 faiss_index/        # 💾 Vector database storage
├── 📁 tests/              # 🧪 Test suite
├── 📄 .env               # 🔐 Environment variables
├── 📄 pyproject.toml     # 📦 Project configuration
├── 📄 requirements.txt   # 📋 Dependencies
├── 📄 test_voice.py      # 🎙️ Voice functionality testing
└── 📄 README.md          # 📖 This file
```

## 🛠️ Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run voice tests
uv run python test_voice.py

# Run with coverage
uv run pytest --cov=src
```

### Code Quality

```bash
# Format code
uv run black src/

# Lint code
uv run ruff check src/

# Type checking
uv run mypy src/
```

### Adding New Features

1. **Voice Features**: Extend `src/voice_handler.py`
2. **UI Components**: Modify `src/streamlit_app.py`
3. **LLM Logic**: Update `src/chatbot.py`
4. **Document Processing**: Enhance `src/pdf_loader.py`

## 🔧 Troubleshooting

### Voice Issues

**🎤 Microphone Not Working**
- Check microphone permissions in system settings
- Try different microphone/headset
- Install PyAudio: `pip install pyaudio`
- Test with: `uv run python test_voice.py`

**🔊 Text-to-Speech Not Working**
- Verify speakers/headphones are functional
- Check system audio settings
- Update audio drivers (Windows)
- Test TTS button in the app

**🌐 Speech Recognition Errors**
- Speak clearly at normal volume
- Minimize background noise
- Ensure internet connection (Google API)
- Try different accents/languages

### Common Errors

**❌ "GROQ_API_KEY not set"**
```bash
# Check .env file exists and contains valid key
cat .env
# Get free key at: https://console.groq.com
```

**❌ "Vector store creation failed"**
- Verify PDF files exist in `data/` folder
- Check file permissions
- Ensure sufficient disk space

**❌ "Could not find PyAudio"**
- Normal behavior - app works without PyAudio
- Install for enhanced microphone support:
  ```bash
  pip install pyaudio
  ```

**❌ "Module not found" errors**
```bash
# Reinstall dependencies
uv sync --reinstall
```

## 📊 Performance Tips

- **Large Documents**: Increase `CHUNK_SIZE` for better context
- **Fast Responses**: Use `llama3.1-8b-instant` model
- **Accuracy**: Use `llama3.1-405b-instruct` for complex queries
- **Memory**: Clear vector store periodically for large document sets

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Use type hints
- Test voice features thoroughly

## 📄 License

**MIT License** - See [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

- **LangChain** - LLM framework
- **FAISS** - Vector similarity search
- **Groq** - Ultra-fast LLM inference
- **Streamlit** - Web app framework
- **HuggingFace** - Embeddings models
- **Google Speech API** - Speech recognition

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- **Documentation**: [Wiki](https://github.com/your-repo/wiki)

---

**Built with ❤️ using modern AI and voice technologies**

### Streamlit UI Features

- 🎨 **User-friendly interface** with chat history
- 📄 **Source citations** with document previews
- 📱 **Responsive design** that works on desktop and mobile
- ⚙️ **Settings panel** for configuration
- 🗑️ **Chat history management**
- 📚 **Help documentation** built-in

### Interactive Chat (CLI)

Once running in CLI mode, you can:
- Ask questions about your documents
- Get answers with source citations
- Type `exit` or `quit` to end the session

### Example

```
You: What is the main topic of the document?

Bot: The main topic is... [answer based on documents]

Sources:
  1. Page 2
  2. Page 5
```

## Project Structure

```
RAG_Chatbot/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── config.py            # Configuration management
│   ├── pdf_loader.py        # PDF loading and processing
│   ├── vector_store.py      # FAISS vector store management
│   ├── chatbot.py           # RAG chatbot logic
│   └── main.py              # CLI entry point
├── streamlit_app.py         # Streamlit UI
├── data/                    # PDF files (add your PDFs here)
├── faiss_index/             # Vector store (auto-generated)
├── pyproject.toml           # Project dependencies (UV)
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Configuration

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `LLM_MODEL`: Model to use (default: gpt-3.5-turbo)
- `CHUNK_SIZE`: Size of document chunks (default: 1000)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 200)

## Features

✅ PDF Loading and Processing  
✅ FAISS Vector Store Integration  
✅ LangChain RetrievalQA Chain  
✅ OpenAI GPT Integration  
✅ Source Document Citations with Previews  
✅ **Streamlit Web UI** for easy interaction  
✅ CLI mode for terminal-based usage  
✅ Chat history management  
✅ Responsive and intuitive interface  

## Development

### Running Tests

```bash
uv run pytest
```

### Code Formatting

```bash
uv run black src/
```

### Linting

```bash
uv run ruff check src/
```

## Troubleshooting

### No PDFs found error
- Make sure PDF files are in the `data/` folder
- Check file permissions

### OpenAI API key errors
- Verify `OPENAI_API_KEY` is set in `.env`
- Check your API key is valid

### Vector store issues
- Delete `faiss_index/` folder to rebuild from scratch
- Ensure sufficient disk space

## License

MIT

## Support

For issues or questions, please refer to the documentation or create an issue in the repository.

