import streamlit as st
from main import chatbot

st.set_page_config(
    page_title = "RAG Chatbot",
    
)

st.title("RAG Chatbot")

question = st.text_input(
    "Ask something about the document"
)

if st.button("Ask"):
    with st.spinner("Thinking...."):
        answer = chatbot(question)
    st.write(answer)