def route_prompt(intent):
    if intent == "summarization":
        return "You are a prompt engineer. Your job is to rewrite prompts specifically for summarization tasks."
    elif intent == "coding":
        return "You are a prompt engineer. Your job is to rewrite prompts specifically for coding tasks."
    elif intent == "explanation":
        return "You are a prompt engineer. Your job is to rewrite prompts specifically for explanation tasks."
    return "You are a prompt engineer. Rewrite prompts to be clear, specific, and effective."