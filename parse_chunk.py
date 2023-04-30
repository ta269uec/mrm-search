import pickle

from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def docs_from_pdf(file_path, chunk_size=1000, chunk_overlap=0):
    data = UnstructuredPDFLoader(file_path).load()
    return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap).split_documents(data)

def serialize_docs(file_path, docs):
    with open(file_path, "wb") as fd:
        pickle.dump(docs, fd)
