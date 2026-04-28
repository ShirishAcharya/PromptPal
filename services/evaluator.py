from services.llm import call_llm

def evaluate_prompt(prompt):
    messages = [
        {"role": "system", "content": "You evaluate prompts."},
        {"role": "user", "content": f"""
        
        Evaluate ONLY the quality of this prompt.

        Do not assume it is empty unless it actually is.

        Return JSON:
        {{
            "score": 0-10,
            "feedback": "..."
        }}

        Prompt: {prompt}
        """}
    ]
    return call_llm(messages)