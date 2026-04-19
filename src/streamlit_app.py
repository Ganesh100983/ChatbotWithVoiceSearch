"""Streamlit UI for RAG Chatbot."""

import streamlit as st
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config import validate_config, DATA_DIR, VECTOR_STORE_PATH
from src.pdf_loader import PDFLoader
from src.vector_store import FAISSVectorStore
from src.chatbot import RAGChatbot
from src.voice_handler import voice_handler


def initialize_session_state():
    """Initialize Streamlit session state."""
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "vector_store_loaded" not in st.session_state:
        st.session_state.vector_store_loaded = False
    if "voice_listening" not in st.session_state:
        st.session_state.voice_listening = False
    if "voice_enabled" not in st.session_state:
        st.session_state.voice_enabled = True
    if "tts_enabled" not in st.session_state:
        st.session_state.tts_enabled = True


def handle_voice_input(text: str):
    """Handle voice input by processing it as a chat message."""
    if text.strip():
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": f"🎤 {text}"})

        # Process the query
        process_chat_message(text)


def process_chat_message(prompt: str):
    """Process a chat message and generate response."""
    # Get bot response
    response = st.session_state.chatbot.answer(prompt)

    # Add bot response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response["answer"],
        "sources": response.get("sources", []),
    })

    # Speak response if TTS is enabled
    if st.session_state.tts_enabled and response["success"]:
        voice_handler.speak(response["answer"])


def toggle_voice_listening():
    """Toggle voice listening on/off."""
    if st.session_state.voice_listening:
        # Stop listening
        voice_handler.stop_listening()
        st.session_state.voice_listening = False
    else:
        # Start listening
        if voice_handler.start_listening(handle_voice_input):
            st.session_state.voice_listening = True
        else:
            st.error("Failed to start voice listening")
    if "voice_listening" not in st.session_state:
        st.session_state.voice_listening = False
    if "voice_enabled" not in st.session_state:
        st.session_state.voice_enabled = True
    if "tts_enabled" not in st.session_state:
        st.session_state.tts_enabled = True


def load_vector_store():
    """Load or create vector store."""
    try:
        vector_store = FAISSVectorStore()

        # Check if vector store already exists
        if vector_store.exists():
            with st.spinner("Loading vector store..."):
                vector_store.load_vector_store()
                st.session_state.vector_store_loaded = True
                return vector_store

        # Create new vector store from PDFs
        st.warning("Vector store not found. Checking for PDF files...")

        pdf_loader = PDFLoader()
        documents = pdf_loader.process_pdfs(str(DATA_DIR))

        if not documents:
            st.error("No PDF documents found in the 'data' folder. Please add PDF files.")
            return None

        with st.spinner(f"Creating vector store with {len(documents)} document chunks..."):
            vector_store.create_vector_store(documents)
            vector_store.save_vector_store()
            st.session_state.vector_store_loaded = True
            st.success("Vector store created successfully!")

        return vector_store

    except Exception as e:
        st.error(f"Error loading vector store: {str(e)}")
        return None


def main():
    """Main Streamlit app."""
    st.set_page_config(
        page_title="RAG Chatbot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS
    st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stChatMessage {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.5rem;
    }
    .source-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("🤖 RAG Chatbot")
    st.markdown("#### Chat with your PDF documents using AI")

    # Initialize session state
    initialize_session_state()

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")

        # Vector store status
        st.subheader("Vector Store Status")
        vector_store_status = "✅ Ready" if st.session_state.vector_store_loaded else "❌ Not Loaded"
        st.markdown(f"**Status:** {vector_store_status}")

        # Load button
        if st.button("🔄 Load/Create Vector Store", use_container_width=True):
            with st.spinner("Processing..."):
                vector_store = load_vector_store()
                if vector_store:
                    st.session_state.chatbot = RAGChatbot(vector_store)
                    st.success("Chatbot ready!")

        st.divider()

        # Voice Settings
        st.subheader("🎤 Voice Settings")

        # Voice input toggle
        voice_col1, voice_col2 = st.columns(2)
        with voice_col1:
            st.session_state.voice_enabled = st.checkbox(
                "Enable Voice Input",
                value=st.session_state.voice_enabled,
                help="Allow voice input using microphone"
            )

        with voice_col2:
            st.session_state.tts_enabled = st.checkbox(
                "Enable Text-to-Speech",
                value=st.session_state.tts_enabled,
                help="Speak bot responses aloud"
            )

        # Voice listening button
        if st.session_state.voice_enabled and st.session_state.chatbot is not None:
            if st.session_state.voice_listening:
                if st.button("🔴 Stop Voice Listening", use_container_width=True):
                    toggle_voice_listening()
                    st.rerun()
            else:
                if st.button("🎤 Start Voice Listening", use_container_width=True):
                    toggle_voice_listening()
                    st.rerun()

            # Voice status
            if st.session_state.voice_listening:
                st.success("🎤 Listening... Speak now!")
            else:
                st.info("Click 'Start Voice Listening' to use voice input")

        st.divider()

        # Information
        st.subheader("📚 Information")
        with st.expander("How to use"):
            st.markdown("""
            1. **Add PDFs**: Place PDF files in the `data/` folder
            2. **Load Vector Store**: Click the load button
            3. **Ask Questions**: Type your questions or use voice input
            4. **View Sources**: See which documents provided the answer

            **Voice Features:**
            - 🎤 **Voice Input**: Click "Start Voice Listening" to speak questions
            - 🔊 **Text-to-Speech**: Bot responses are spoken aloud (if enabled)
            - ⚙️ **Voice Settings**: Configure voice input/output in the sidebar
            """)

        with st.expander("About"):
            st.markdown("""
            **RAG Chatbot** uses:
            - **LangChain**: LLM framework
            - **FAISS**: Vector database
            - **Groq**: Language model (fast LLM inference)
            - **HuggingFace**: Embeddings model
            - **Streamlit**: User interface
            - **Speech Recognition**: Voice input processing
            - **pyttsx3**: Text-to-speech output
            """)

    # Main content
    st.divider()

    # Check if chatbot is ready
    if st.session_state.chatbot is None:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.info("👈 Load the vector store to get started!")

        # Try to auto-load
        if st.button("Auto-Load Vector Store", use_container_width=True, key="auto_load"):
            try:
                validate_config()
                vector_store = load_vector_store()
                if vector_store:
                    st.session_state.chatbot = RAGChatbot(vector_store)
                    st.rerun()
            except ValueError as e:
                st.error(f"Configuration Error: {str(e)}")
    else:
        # Display chat messages
        chat_container = st.container()

        with chat_container:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

                    # Display sources if available
                    if "sources" in message and message["sources"]:
                        with st.expander("📄 View Sources"):
                            for i, source in enumerate(message["sources"], 1):
                                col1, col2 = st.columns([1, 4])
                                with col1:
                                    st.caption(f"Source {i}")
                                with col2:
                                    page_num = source.metadata.get("page", "N/A")
                                    st.caption(f"Page {page_num}")
                                st.markdown(f"> {source.page_content[:200]}...")

        st.divider()

        # Chat input area
        input_col1, input_col2 = st.columns([4, 1])

        with input_col1:
            prompt = st.chat_input(
                "Ask a question about your documents..." +
                (" (Voice input active 🎤)" if st.session_state.voice_listening else "")
            )

        with input_col2:
            if st.session_state.tts_enabled and st.button("🔊 Test TTS", help="Test text-to-speech"):
                voice_handler.speak("Hello! This is a test of the text-to-speech feature.")

        # Process text input
        if prompt:
            # Add user message to history
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)

            # Process the message
            process_chat_message(prompt)

            # Rerun to update the chat display
            st.rerun()


if __name__ == "__main__":
    try:
        validate_config()
        main()
    except ValueError as e:
        st.error(f"⚠️ Configuration Error: {str(e)}")
        st.write("Please set up your `.env` file with the required API keys.")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
