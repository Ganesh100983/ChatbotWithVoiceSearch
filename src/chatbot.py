"""Main RAG Chatbot module."""

from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.config import LLM_MODEL
from src.vector_store import FAISSVectorStore


class RAGChatbot:
    """RAG-based Chatbot using LangChain and FAISS."""

    def __init__(self, vector_store: FAISSVectorStore, temperature: float = 0.7):
        """Initialize RAG Chatbot.
        
        Args:
            vector_store: FAISS vector store instance
            temperature: Temperature for LLM responses (0-1)
        """
        self.vector_store = vector_store
        self.temperature = temperature
        
        # Initialize LLM (OpenAI)
        self.llm = ChatOpenAI(
            model=LLM_MODEL,
            temperature=temperature,
        )
        
        # Initialize retriever
        self.retriever = self.vector_store.as_retriever()
        
        # Initialize QA chain
        self.qa_chain = self._create_qa_chain()

    def _create_qa_chain(self):
        """Create the RAG chain using LCEL.
        
        Returns:
            Chain instance
        """
        prompt_template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context:
{context}

Question: {question}
Answer:"""

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        # Create a simple chain using LCEL
        def format_docs(docs):
            return "\n\n".join([doc.page_content for doc in docs])

        chain = (
            {
                "context": self.retriever | format_docs,
                "question": RunnablePassthrough(),
            }
            | prompt
            | self.llm
        )

        return chain

    def answer(self, query: str) -> dict:
        """Get answer to a query.
        
        Args:
            query: User query
            
        Returns:
            Dictionary with answer and source documents
        """
        try:
            # Get relevant documents
            docs = self.retriever.invoke(query)
            
            # Get answer from LLM
            answer_text = self.qa_chain.invoke(query)
            
            # Extract text from response
            if hasattr(answer_text, 'content'):
                answer = answer_text.content
            else:
                answer = str(answer_text)
            
            return {
                "answer": answer,
                "sources": docs,
                "success": True,
            }
        except Exception as e:
            return {
                "answer": f"Error: {str(e)}",
                "sources": [],
                "success": False,
            }

    def chat(self):
        """Interactive chat session."""
        print("\n" + "="*60)
        print("RAG Chatbot - Interactive Mode")
        print("="*60)
        print("Type 'exit' or 'quit' to end the conversation\n")

        while True:
            try:
                user_input = input("You: ").strip()

                if user_input.lower() in ["exit", "quit"]:
                    print("\nGoodbye!")
                    break

                if not user_input:
                    continue

                response = self.answer(user_input)
                
                print(f"\nBot: {response['answer']}\n")

                if response.get("sources"):
                    print("Sources:")
                    for i, doc in enumerate(response["sources"], 1):
                        print(f"  {i}. Page {doc.metadata.get('page', 'N/A')}")
                    print()

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}\n")
