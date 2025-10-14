import streamlit as st
from src.rag_pipeline import RAGPipeline

st.title("Smart Document Q&A Assistant")

pipeline = RAGPipeline()
pipeline.load_documents("data/sample_docs/")

uploaded_files = st.file_uploader(
    "Upload documents (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True
)
query = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if query:
        answer = pipeline.answer_query(query)
        st.write("Answer:", answer)
    else:
        st.write("Please enter a question.")
