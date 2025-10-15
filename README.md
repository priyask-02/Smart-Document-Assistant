# Smart-Document-Assistant
Generative AI Project for RAG to documents


https://priyask-02-smart-document-assistant.streamlit.app


A Streamlit-based application that allows users to upload PDF and DOCX documents and ask questions. Powered by **LangChain**, **OpenAI embeddings**, and a **RAG (Retrieval-Augmented Generation) pipeline**.

docs/Document_Assistant.jpg

*Example interface showing document upload and question answering*

## 🌟 Features
- Upload PDFs or DOCX documents
- Ask natural language questions about your documents
- Answers include source references
- Real-time interactive UI powered by Streamlit
- Handles multiple documents in a single session


## 🔗 Live Demo
Try it out online: [Streamlit Cloud App](https://priyask-02-smart-document-assistant.streamlit.app)


## 🗂 Project Structure
Smart-Document-Assistant/
├─ demo_app/ # Streamlit app
│ └─ streamlit_app.py
├─ src/ # Core RAG pipeline and utilities
│ ├─ rag_pipeline.py
│ └─ utils.py
├─ data/ # Sample PDFs/DOCX files (optional)
├─ docs/ # Screenshots, GIFs, or documentation
├─ requirements.txt
└─ README.md