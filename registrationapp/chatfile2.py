import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import UnstructuredURLLoader

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.schema import Document
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

# Load API Key Securely
load_dotenv()  # Loads variables from .env file
api_key = 'AIzaSyAWVYIr5kfzQoJASmP4fYzdiJfUvgDa_9U'
if not api_key:
    raise ValueError("Google API Key not found in environment variables.")
os.environ["GOOGLE_API_KEY"] = api_key

# Global Variables
vector_store = None
vector_store_url = None
vector_store_pdf = None
conv = None
agent = None

def web(urls):
    """Loads text data from URLs and creates FAISS vector store."""
    global vector_store_url
    try:
        print("Loading web data...")
        loaders = UnstructuredURLLoader(urls=urls)
        data = loaders.load()

        splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=300,  # Adjusted chunk size
            chunk_overlap=50,  # Adjusted overlap
        )
        docs = splitter.split_documents(data)

        embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store_url = FAISS.from_documents(docs, embedding)
        print("Web data loaded successfully!")
    except Exception as e:
        print(f"Error in web(): {e}")

def read_pdf(pdfs):
    """Reads PDF files, extracts text, and creates FAISS vector store."""
    global vector_store_pdf
    try:
        text = ""
        for pdf in pdfs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text:
            raise ValueError("No text extracted from PDF.")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,  # Adjusted chunk size
            chunk_overlap=50,  # Adjusted overlap
        )
        docs = splitter.split_text(text)

        embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store_pdf = FAISS.from_texts(docs, embedding)
        print("PDF data loaded successfully!")
    except Exception as e:
        print(f"Error in read_pdf(): {e}")

def chat_connection():
    """Initializes the chat system by merging FAISS indexes and setting up LLM chain."""
    global vector_store, vector_store_url, vector_store_pdf, conv, agent

    if vector_store_url and vector_store_pdf:
        vector_store_url.merge_from(vector_store_pdf)
        vector_store = vector_store_url
    elif vector_store_url:
        vector_store = vector_store_url
    elif vector_store_pdf:
        vector_store = vector_store_pdf
    else:
        print("No data available for retrieval.")
        return

    try:
        agent = ChatGoogleGenerativeAI(model='gemini-1.5-pro', convert_system_message_to_human=True)
        conv = RetrievalQAWithSourcesChain.from_llm(llm=agent, retriever=vector_store.as_retriever())
        print("Chat connection established successfully!")
    except Exception as e:
        print(f"Error in chat_connection(): {e}")

def chatnew(chat):
    """Processes user queries and returns AI-generated responses."""
    global conv
    if conv is None:
        return "Chat system is not initialized. Please call chat_connection() first."

    try:
        response = conv.invoke({"question": chat})
        return response.get('answer', "No response received.")
    except Exception as e:
        return f"Error in chatnew(): {e}"

# Example Usage
web(["https://en.wikipedia.org/wiki/French_Revolution"])
chat_connection()
print(chatnew("What is the French Revolution?"))
