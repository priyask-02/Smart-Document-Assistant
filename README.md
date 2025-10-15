# Smart-Document-Assistant
Generative AI Project for RAG to documents

A Streamlit-based application that allows users to upload PDF and DOCX documents and ask questions. Powered by **LangChain**, **OpenAI embeddings**, and a **RAG (Retrieval-Augmented Generation) pipeline**.

## 🌟 Features
- Upload PDFs or DOCX documents
- Ask natural language questions about your documents
- Answers include source references
- Real-time interactive UI powered by Streamlit
- Handles multiple documents in a single session

https://smart-document-assistant-x9q2c5ww4lv9pqtqhuwmji.streamlit.app/

🧩 How It Works
- Upload documents → PDFs or DOCX are split into chunks.
- Chunks embedded using OpenAI embeddings
- Embeddings stored in Chroma vector store.
- Ask a question → RAG pipeline retrieves relevant chunks
- Answers displayed with sources in the Streamlit interface.

🙋 My Contributions
- Built RAG pipeline with LangChain & OpenAI embeddings
- Developed interactive Streamlit interface
- Handled PDF & DOCX parsing, chunking, source tracking
- Configured Streamlit Cloud deployment & secrets management
- Created a reproducible environment with requirements.txt
