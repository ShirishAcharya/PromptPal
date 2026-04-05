import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def enhance_prompt(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful prompt engineer. Given a rough prompt, rewrite it to be more effective and detailed for use with a large language model like ChatGPT."},
            {"role": "user", "content": f"Original prompt: {user_input}\n\nImproved prompt:"}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    print("PromptPal: Enhance your prompts for better LLM responses using OpenRouter!")
    user_input = input("Enter your rough prompt: ")
    improved = enhance_prompt(user_input)
    print("\n Enhanced Prompt:")
    print(improved)
