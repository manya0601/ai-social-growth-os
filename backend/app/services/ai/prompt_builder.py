def build_tweet_prompt(
    topic: str,
    context: list
):

    memory_context = "\n".join(
        [item["payload"]["content"] for item in context]
    )

    prompt = f"""
    Generate a viral Twitter/X post.

    Topic:
    {topic}

    Relevant Context:
    {memory_context}

    Requirements:
    - high engagement
    - concise
    - curiosity-driven
    - human tone
    """

    return prompt

