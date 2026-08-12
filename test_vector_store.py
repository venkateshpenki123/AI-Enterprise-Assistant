from vector_store import (
    create_embeddings,
    create_faiss_index,
    search_documents
)


# Sample document chunks
chunks = [
    "Artificial Intelligence is used in many industries.",

    "Machine Learning allows computers to learn patterns from data.",

    "Generative AI can generate text, images and code.",

    "RAG combines document retrieval with Generative AI."
]


print("Creating embeddings...")

embeddings = create_embeddings(chunks)

print(
    "Embedding shape:",
    embeddings.shape
)


print("\nCreating FAISS index...")

index = create_faiss_index(
    embeddings
)

print(
    "FAISS index created successfully!"
)


# Test question
question = "What is machine learning?"

print("\nSearching documents...")

results = search_documents(
    question,
    chunks,
    index,
    top_k=2
)


print("\nRelevant Documents:")

for i, result in enumerate(results):

    print("--------------------")

    print(
        f"Result {i + 1}:"
    )

    print(result)