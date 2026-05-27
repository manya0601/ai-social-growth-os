from app.services.retrieval_service import search_memory

from app.services.ai.prompt_builder import build_tweet_prompt

from app.services.ai.ai_gateway import generate_ai_response

def generate_tweet(
    topic: str
):

    context = search_memory(topic)

    prompt = build_tweet_prompt(
        topic,
        context
    )

    result = generate_ai_response(
        task_type="tweet_generation",
        prompt=prompt
    )

    return result