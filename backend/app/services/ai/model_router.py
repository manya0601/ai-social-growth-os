def select_model(task_type: str):

    routing = {

        "tweet_generation": "claude",

        "linkedin_generation": "gpt",

        "trend_analysis": "gemini",

        "fast_reply": "haiku"
    }

    return routing.get(

        task_type,

        "claude"
    )

