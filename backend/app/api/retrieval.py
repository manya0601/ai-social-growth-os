from fastapi import APIRouter, HTTPException

from app.services.retrieval_service import list_memories

router = APIRouter()


@router.get("/search-memory")
def search_memory_route():
    try:
        return list_memories()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

