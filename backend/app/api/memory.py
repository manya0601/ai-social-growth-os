from fastapi import APIRouter, Query

from app.services.memory_service import store_memory

router = APIRouter()

@router.post("/store-memory")
async def add_memory():

    sample_content = """
    AI startups using viral short-form videos
    are growing faster on Twitter/X than traditional blogs.
    """

    metadata = {
        "platform": "twitter",
        "category": "trend",
        "engagement_score": 92
    }

    result = store_memory(
        sample_content,
        metadata
    )

    return result


# ADD THIS NEW ROUTE
@router.get("/search-memory")
async def search_memory(query: str = Query(...)):

    return {
        "searched_query": query
    }