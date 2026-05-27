from app.core.qdrant_client import client

COLLECTION_NAME = "social_memory"

def list_memories(limit: int = 10):
    results, _ = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=limit,
        with_payload=True,
        with_vectors=False
    )

    return [{"id": str(point.id), "payload": point.payload} for point in results]