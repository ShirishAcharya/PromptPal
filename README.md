# PromptPal – LLM Workflow Engine

PromptPal is a multi-step LLM workflow engine that transforms raw user prompts into optimized, structured prompts using an agentic pipeline. The system performs intent detection, prompt routing, structured generation, and quality evaluation.

Unlike traditional prompt enhancers that perform a single transformation, PromptPal is designed as a workflow-based system that simulates decision-making and evaluation loops.

## Overview

PromptPal processes user input through a structured pipeline:

1. Intent classification
2. Prompt routing based on intent
3. Prompt generation and optimization
4. Automated quality evaluation

The goal is to produce high-quality, structured prompts suitable for use with large language models.

## Architecture

The system follows a multi-stage pipeline:

Input → Intent Detection → Routing → Prompt Generation → Evaluation → Output

## Features

- Intent classification for user input
- Dynamic routing based on detected intent
- LLM-based prompt optimization
- Structured JSON output generation
- Automated prompt quality evaluation
- Streamlit-based interactive interface

## Project Structure
```bash 
promptpal/
├── app.py
├── main.py
├── services/
│ ├── llm.py
│ ├── intent.py
│ ├── router.py
│ ├── generator.py
│ ├── evaluator.py
├── workflows/
│ └── prompt_workflow.py
├── requirements.txt
├── .env
├── venv/
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

## Example

### Input
explain neural networks simply

### Output

**Enhanced Prompt:**
Explain the concept of neural networks in a way that is understandable to beginners with no prior knowledge of machine learning. Include a step-by-step explanation of how neural networks process information, including neurons, layers, activation functions, and training mechanisms.

**Intent:**
explanation

**Quality Score:**
10/10

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
streamlit run streamlit_app.py
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
