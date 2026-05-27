from fastapi import APIRouter

from app.services.competitor_memory_service import ingest_competitor_posts

router = APIRouter()

@router.post("/ingest-competitor-posts")
async def ingest_posts():

    result = ingest_competitor_posts()

    return result