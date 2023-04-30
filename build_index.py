import pickle

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def deserialize_docs(file_path):
    with open(file_path, "rb") as fd:
        return pickle.load(fd)

def get_sentence_embedder(model_name="all-MiniLM-L6-v2"):
    return HuggingFaceEmbeddings(model_name=model_name)

def build_index_from_doc_files(file_name_docs, persist_directory):
    vectordb = Chroma.from_documents(documents=deserialize_docs(file_name_docs),\
                                     embedding=get_sentence_embedder(),\
                                     persist_directory=persist_directory)
    vectordb.persist()
    return

def load_index_from_disk(persist_directory):
    return Chroma(persist_directory=persist_directory, embedding_function=get_sentence_embedder())