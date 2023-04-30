import streamlit as st
from io import StringIO
from build_index import *
from qa import initialize_retriever, list_relevant_docs

st.header("Model Risk Management Search Engine")
query = False

vectordb = load_index_from_disk(persist_directory="Data/")
engine = initialize_retriever(vectordb)

query = st.text_input("Enter your question")
button = st.button("Submit")
  
if button and query:
    with st.spinner("Searching for the answer..."):
        for ans in list_relevant_docs(query, engine):
            st.success(ans.page_content)