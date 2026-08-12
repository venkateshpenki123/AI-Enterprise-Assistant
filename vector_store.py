import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create embeddings
def create_embeddings(chunks):

    embeddings = model.encode(chunks)

    embeddings = np.array(
        embeddings
    ).astype("float32")

    return embeddings


# Create FAISS index
def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(embeddings)

    return index


# Create complete vector store
def create_vector_store(chunks):

    embeddings = create_embeddings(
        chunks
    )

    index = create_faiss_index(
        embeddings
    )

    return index


# Search documents
def search_documents(
    query,
    chunks,
    index,
    top_k=3
):

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for i in indices[0]:

        if i < len(chunks):

            results.append(
                chunks[i]
            )

    return results