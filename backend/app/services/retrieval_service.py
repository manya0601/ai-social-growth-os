from app.core.qdrant_client import client
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "social_memory"

model = SentenceTransformer("all-MiniLM-L6-v2")


def list_memories(limit: int = 10):
    results, _ = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=limit,
        with_payload=True,
        with_vectors=False
    )

    return [{"id": str(point.id), "payload": point.payload} for point in results]


def search_memory(query: str, limit: int = 5):
    query_vector = model.encode(query).tolist()

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=limit
    )

    return [
        {
            "id": str(point.id),
            "score": point.score,
            "payload": point.payload
        }
        for point in results
    ]