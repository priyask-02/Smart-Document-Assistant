import sys
import os


# Rebuild trigger on 2025-10-15

# Add the parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import warnings
warnings.filterwarnings("ignore", message="missing ScriptRunContext")


import streamlit as st
from src.rag_pipeline import RAGPipeline
import tempfile
import os

st.title("Smart Document Q&A Assistant")

pipeline = RAGPipeline()

uploaded_files = st.file_uploader("Upload documents (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)
query = st.text_input("Ask your question:")

if uploaded_files:
    temp_dir = tempfile.mkdtemp()
    for uploaded_file in uploaded_files:
        path = os.path.join(temp_dir, uploaded_file.name)
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    pipeline.load_documents(temp_dir)
    st.success(f"Loaded {len(uploaded_files)} documents!")

if st.button("Get Answer") and query:
    answer, sources = pipeline.answer_query(query)
    st.subheader("Answer:")
    st.write(answer)
    st.subheader("Source Documents:")
    st.write(", ".join(set(sources)))  # show unique filenames

answer, sources = pipeline.answer_query(query)