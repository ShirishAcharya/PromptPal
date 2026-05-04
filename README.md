# PromptPal

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?logo=streamlit&logoColor=white)

PromptPal is a multi-step LLM workflow engine that transforms rough, vague prompts into structured, optimized ones. It runs the input through an agentic pipeline — classifying intent, routing to the right system prompt, generating an enhanced version, and evaluating the result.

Unlike single-step prompt enhancers, PromptPal treats the whole process as a workflow with distinct, replaceable stages.

## Overview

Every prompt runs through four steps:

1. **Intent classification** — determines what the user is trying to do
2. **Routing** — selects a specialized system prompt based on the intent
3. **Generation** — rewrites the input into a structured, detailed prompt
4. **Evaluation** — scores the output and provides feedback on clarity and completeness

## Architecture

The system follows a multi-stage pipeline:

Input → Intent Detection → Routing → Prompt Generation → Evaluation → Output

## Demo 


https://github.com/user-attachments/assets/c135bd27-273a-499b-9adf-bd2617921e4c


## Features

- Intent classification across multiple categories (explanation, coding, summarization and general)
- Dynamic routing so each intent gets a purpose-built system prompt
- LLM-based prompt optimization and structured output
- Automated quality scoring with written feedback
- Modular Streamlit frontend split across components and a shared theme

## Project Structure

```bash
promptpal/
├── app.py                      # Entrypoint — wires components together
├── main.py                     # CLI runner for quick testing
├── styles/
│   └── theme.py                # All CSS in one place
├── components/
│   ├── header.py               # Page title and subtitle
│   ├── input_section.py        # Prompt input and run button
│   ├── metrics.py              # Intent, score, and word count cards
│   └── results.py              # Enhanced prompt, feedback, raw JSON
├── services/
│   ├── intent.py               # Intent classification
│   ├── router.py               # System prompt selection
│   ├── generator.py            # Prompt generation
│   └── evaluator.py            # Quality evaluation
├── workflow/
│   └── prompt_workflow.py      # Pipeline orchestration
├── requirements.txt
└── .env
```

## Workflow Description

### 1. Intent Classification
The system analyzes the user input and classifies it into predefined categories such as explanation, coding, summarization, or general.

### 2. Prompt Routing
Based on the detected intent, a specialized system prompt is selected to guide the optimization process.

### 3. Prompt Generation
The input is transformed into a structured, detailed, and optimized prompt using an LLM.

### 4. Evaluation
The generated prompt is evaluated for clarity, specificity, and completeness, producing a quality score and feedback.

## Setup Instructions

Clone the repository:


1. Clone the repository
``` bash
git clone https://github.com/ShirishAcharya/promptpal.git
cd promptpal
```
2. Create virtual environment
``` bash
python -m venv venv
```
**Linux/macOS**
``` bash
source venv/bin/activate
```
**Windows**
``` bash
venv\Scripts\activate
```
3. Install dependencies
``` bash
pip install -r requirements.txt
```
4. Get your API key from openrouter or any other service you might prefer


Create a .env file with this content:
```
OPENROUTER_API_KEY=sk-or-XXXXXXXXXXXXXXXX
```
5. Run app
``` bash
streamlit run app.py
```
Open http://localhost:8501



## Design Philosophy

PromptPal is built around the concept of treating LLM interactions as workflows rather than single-step prompts. It introduces structure, modularity, and evaluation into prompt engineering.

The system demonstrates:

- Separation of concerns in LLM pipelines
- Intent-aware processing
- Structured output generation
- Evaluation-driven refinement

## Future Improvements

- Retry mechanism for low-quality outputs
- Multi-prompt generation and ranking
- Memory layer for prompt history
- Tool-calling integration
- Multi-agent orchestration

## License

MIT License
