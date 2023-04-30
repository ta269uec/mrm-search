import streamlit as st
from io import StringIO
#from vector_search import *
#import qa
#from utils import *

st.header("Model Risk Management Search Engine")
query = False

query = st.text_input("Enter your question")
button = st.button("Submit")
  
if button and query:
    with st.spinner("Searching for the answer..."):
        st.success("Answer: "+ "This is the answer")
        # urls,res = find_match(query,2)
        # context= "\n\n".join(res)
        # st.expander("Context").write(context)
        # prompt = qa.create_prompt(context,query)
        # answer = qa.generate_answer(prompt)
        # st.success("Answer: "+answer)
