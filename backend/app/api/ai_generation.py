from fastapi import APIRouter

from app.services.ai.content_generator import generate_tweet

router = APIRouter()


@router.get("/generate-tweet")
async def generate_ai_tweet(
    topic: str
):

    result = generate_tweet(topic)

    return {
        "generated_content": result
    }

