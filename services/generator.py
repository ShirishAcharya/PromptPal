from services.llm import call_llm

def generate_prompt(user_input, system_prompt, intent):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"""
        You are an expert prompt engineer.

        Your task is to transform a vague or simple prompt into a highly effective, detailed prompt.

        Rules:
        - Do NOT answer the prompt
        - ONLY rewrite it
        - Make it more specific, structured, and useful
        - Add helpful constraints (examples, format, clarity, etc.)
        - Improve clarity and depth significantly

        Intent: {intent}

        Return ONLY valid JSON:
        {{
            "enhanced_prompt": "...",
            "reasoning": "...",
            "suggested_temperature": 0-1
        }}

        Input: {user_input}
        """}
    ]
    return call_llm(messages)