from qdrant_client.models import PointStruct
from uuid import uuid4

from app.core.qdrant_client import client
from app.services.embedding_service import generate_embedding

COLLECTION_NAME = "social_memory"

def store_memory(
    content: str,
    metadata: dict
):

    embedding = generate_embedding(content)

    point = PointStruct(
        id=str(uuid4()),
        vector=embedding,
        payload={
            "content": content,
            **metadata
        }
    )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[point]
    )

    return {
        "status": "stored"
    }