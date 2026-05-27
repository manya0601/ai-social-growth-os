import anthropic

from app.core.config import settings

client = anthropic.Anthropic(
    api_key=settings.ANTHROPIC_API_KEY
)

def generate_claude_response(
    prompt: str,
    model: str = "claude-3-5-sonnet-20241022"
):

    response = client.messages.create(

        model=model,

        max_tokens=1000,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text