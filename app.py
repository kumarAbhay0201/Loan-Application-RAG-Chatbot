import streamlit as st
from chatbot import retrieve_top_docs

st.set_page_config(page_title="Loan Chatbot", page_icon="💬")
st.title(":speech_balloon: Loan Application RAG Chatbot")
st.markdown("Ask any question related to past loan applications.")

col1, col2 = st.columns([4, 1])
with col1:
    query = st.text_input(":mag: Enter your question", placeholder="e.g. How can an unemployed woman get a loan?")

with col2:
    ask = st.button("Ask", key="ask")

if ask:
    if query:
        top_3_docs = retrieve_top_docs(query)

        st.markdown("### :brain: Retrieved Answer")
        for doc in top_3_docs:
            st.markdown(doc)
    else:
        st.warning("Please enter a question to proceed.")
