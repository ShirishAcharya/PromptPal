from services.llm import call_llm

def classify_intent(user_input):
    messages = [
        {"role": "system", "content": "You classify user intent."},
        {"role": "user", "content": f"""
        Classify this input into:
        summarization, coding, explanation, general

        Return JSON:
        {{
            "intent": "...",
            "confidence": 0-1
        }}

        Input: {user_input}
        """}
    ]
    return call_llm(messages)