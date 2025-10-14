from rag_pipeline import RAGPipeline

def main():
    print("Initializing Smart Document Q&A Assistant...")
    pipeline = RAGPipeline()
    # Load documents from the sample_docs folder
    pipeline.load_documents("data/sample_docs/")

    while True:
        query = input("Enter your question (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        answer = pipeline.answer_query(query)
        print("Answer:", answer)

if __name__ == "__main__":
    main()
