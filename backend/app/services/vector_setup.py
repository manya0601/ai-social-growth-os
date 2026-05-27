from qdrant_client.models import Distance, VectorParams

from app.core.qdrant_client import client

def create_collection():
    existing = [c.name for c in client.get_collections().collections]

    if "social_memory" not in existing:
        client.create_collection(
            collection_name="social_memory",

            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    print("Vector collection created.")