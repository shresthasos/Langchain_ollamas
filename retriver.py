from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os


loader = PyPDFLoader("my_documents.pdf")
documents = loader.load()

DB_LOCATION = "./pdf_chroma"
COLLECTION_NAME = "pdf_ch"

embeddings = OllamaEmbeddings(
    model ="mxbai-embed-large"
)

if not os.path.exists(DB_LOCATION):
    splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
    )

    chunks = splitter.split_documents(documents)

   



    vector_store = Chroma(
        collection_name= COLLECTION_NAME,
        persist_directory= DB_LOCATION,
        embedding_function= embeddings
    )
    vector_store.add_documents(chunks)

else:
    vector_store = Chroma(
        collection_name= COLLECTION_NAME,
        persist_directory=DB_LOCATION,
        embedding_function=embeddings

    )


retriever = vector_store.as_retriever(
    search_kwargs = {"k": 5}
)