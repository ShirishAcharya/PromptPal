import os
import requests
import json
import re
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"


def extract_json(content: str):
    try:
        return json.loads(content)
    except:
        pass

    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    return {"raw": content}


def call_llm(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "PromptPal"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": messages
    }

    response = requests.post(BASE_URL, headers=headers, json=data)
    response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]

    return extract_json(content)