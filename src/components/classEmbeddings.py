from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import os

DB_DIRECTORY = './src/db'
os.makedirs(DB_DIRECTORY, exist_ok=True)

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector_store = Chroma(persist_directory=DB_DIRECTORY,embedding_function=embeddings,collection_name="default_collection")