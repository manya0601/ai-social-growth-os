from app.services.ai.providers.openai_provider import generate_openai_response

from app.services.ai.providers.anthropic_provider import generate_claude_response

from app.services.ai.providers.gemini_provider import generate_gemini_response

from app.services.ai.model_router import select_model

def generate_ai_response(
    task_type: str,
    prompt: str
):

    selected_model = select_model(task_type)

    if selected_model == "claude":

        return generate_claude_response(prompt)

    elif selected_model == "gpt":

        return generate_openai_response(prompt)

    elif selected_model == "gemini":

        return generate_gemini_response(prompt)

    else:

        return generate_openai_response(prompt)