#  PromptPal – Prompt Enhancer for LLMs

PromptPal is a Streamlit-based GenAI tool that helps you improve rough prompts for Large Language Models like ChatGPT or Mistral. It rewrites your input into a clearer, more specific, and optimized prompt to get better results.

##  Features
- Streamlit GUI for user-friendly interaction
- Real-time prompt enhancement using OpenRouter API
- Read-only output display for copy/paste
- Secure API key handling via `.env`

##  Tech Stack
- Python
- Streamlit
- OpenRouter API (Mistral model)
- dotenv

##  How it Works
1. User inputs a rough prompt.
2. The app sends it to an LLM with a predefined system prompt.
3. The response is a polished, enhanced prompt shown in a vertical textbox.

##  Example
**Input:** "summarize article on AI in education"  
**Output:** "Provide a concise summary of the key findings and implications from an article discussing the use of artificial intelligence in educational settings."

##  Setup Instructions
1. Clone the repo
2. Create a `.env` file with:
```
OPENROUTER_API_KEY=your-api-key-here
```
3. Run the app:
```
streamlit run app.py
```

---

## 📄 License
MIT License
