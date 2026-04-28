from services.intent import classify_intent
from services.router import route_prompt
from services.generator import generate_prompt
from services.evaluator import evaluate_prompt


def run_prompt_workflow(user_input):
    intent_data = classify_intent(user_input)
    intent = intent_data.get("intent", "general")

    system_prompt = route_prompt(intent)

    generated = generate_prompt(user_input, system_prompt, intent)
    enhanced = generated.get("enhanced_prompt")

    if not enhanced:
        enhanced = generated.get("raw", "")

    evaluation = evaluate_prompt(enhanced)

    return {
        "input": user_input,
        "intent": intent_data,
        "output": generated,
        "evaluation": evaluation
    }