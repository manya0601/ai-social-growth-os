from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def generate_openai_response(
    prompt: str,
    model: str = "gpt-4o-mini"
):

    response = client.chat.completions.create(

        model=model,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content