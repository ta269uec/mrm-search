def initialize_retriever(vectordb):
    return vectordb.as_retriever()

def list_relevant_docs(query, engine):
    return engine.get_relevant_documents(query)