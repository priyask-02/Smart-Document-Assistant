import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import warnings
warnings.filterwarnings("ignore", message="missing ScriptRunContext")


import streamlit as st
from src.rag_pipeline import RAGPipeline
import tempfile


st.title("Smart Document Q&A Assistant")

pipeline = RAGPipeline()

uploaded_files = st.file_uploader("Upload documents (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)
query = st.text_input("Ask your question:")

if uploaded_files:
    temp_dir = tempfile.mkdtemp()
    file_paths = []
    for uploaded_file in uploaded_files:
        path = os.path.join(temp_dir, uploaded_file.name)
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(path)
    
    pipeline.load_documents(temp_dir)
    st.success(f"Loaded {len(file_paths)} documents!")

if st.button("Get Answer") and query:
    answer = pipeline.answer_query(query)
    st.write("Answer:", answer)
