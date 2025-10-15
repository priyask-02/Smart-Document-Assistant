from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
#from utils import parse_pdf, parse_docx
from src.utils import parse_pdf, parse_docx
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI

import streamlit as st
key = st.secrets["OPENAI_API_KEY"]

class RAGPipeline:
    def __init__(self, openai_api_key=None, chunk_size=1000, chunk_overlap=200):
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Missing OpenAI API key. Please set it as OPENAI_API_KEY.")
        
        self.embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
        self.index = None
        self.qa_chain = None
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_documents(self, folder_path):
        import glob

        files = glob.glob(os.path.join(folder_path, "*"))
        all_texts = []
        metadata = []

        for file in files:
            if file.endswith(".pdf"):
                text = parse_pdf(file)
            elif file.endswith(".docx"):
                text = parse_docx(file)
            else:
                continue

            # Chunk the text
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
            )
            chunks = splitter.split_text(text)

            all_texts.extend(chunks)
            metadata.extend([{"source": os.path.basename(file)}] * len(chunks))

        if not all_texts:
            raise ValueError("No PDF or DOCX documents found in folder.")

        # Create FAISS vector store with metadata
        #self.index = FAISS.from_texts(all_texts, self.embeddings, metadatas=metadata)
        self.index = Chroma.from_texts(all_texts, self.embeddings, metadatas=metadata)

        # Set up RetrievalQA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0),
            retriever=self.index.as_retriever(),
            return_source_documents=True  # important to see source docs
        )

    def answer_query(self, query):
        if not self.qa_chain:
            return "The model is not initialized yet.", []
    
        result = self.qa_chain.invoke(query)

        answer = result["result"] if "result" in result else result
        sources = []
        if "source_documents" in result:
            sources = [doc.metadata.get("source", "Unknown") for doc in result["source_documents"]]

        return answer, sources  # ✅ exactly two items
