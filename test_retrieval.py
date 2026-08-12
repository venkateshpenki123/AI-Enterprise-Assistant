from vector_store import (
    create_vector_store,
    search_documents
)


# Sample document chunks
chunks = [
    "The company provides health insurance to all full-time employees.",

    "Employees receive 20 days of paid annual leave every year.",

    "The company working hours are 9 AM to 6 PM from Monday to Friday.",

    "Employees can work remotely two days per week with manager approval."
]


print("Creating FAISS vector store...")

index = create_vector_store(
    chunks
)

print("FAISS vector store created successfully!")


# Ask a question
question = input(
    "\nEnter your question: "
)


# Search FAISS
results = search_documents(
    question,
    chunks,
    index,
    top_k=3
)


print("\n==============================")
print("RELEVANT DOCUMENT CHUNKS")
print("==============================")


for i, result in enumerate(results):

    print(
        f"\nResult {i + 1}:"
    )

    print(result)