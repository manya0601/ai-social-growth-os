from fastapi import APIRouter

router = APIRouter()

@router.get("/get-tweets")
async def get_tweets():
    return {"message": "Tweets fetched"}