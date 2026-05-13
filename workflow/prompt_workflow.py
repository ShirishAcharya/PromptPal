from services.intent import classify_intent
from services.router import route_prompt
from services.generator import generate_prompt
from services.evaluator import evaluate_prompt

MAX_RETRIES = 3
SCORE_THRESHOLD = 7

def run_prompt_workflow(user_input):
    intent_data = classify_intent(user_input)
    intent = intent_data.get("intent", "general")
    system_prompt = route_prompt(intent)

    best_result = None
    attempts = 0

    current_input = user_input

    while attempts < MAX_RETRIES:
        generated = generate_prompt(current_input, system_prompt, intent)
        enhanced = generated.get("enhanced_prompt") or generated.get("raw", "")
        evaluation = evaluate_prompt(enhanced)
        score = evaluation.get("score", 0)

        current_result = {
            "input": user_input,
            "intent": intent_data,
            "output": generated,
            "evaluation": evaluation,
            "attempts": attempts + 1
        }

        if best_result is None or score > best_result["evaluation"].get("score", 0):
            best_result = current_result

        if score >= SCORE_THRESHOLD:
            break

        # Feed the feedback back in so the next attempt improves on it
        feedback = evaluation.get("feedback", "")
        current_input = f"{user_input}\n\nPrevious attempt scored {score}/10. Feedback: {feedback}. Improve on this."
        attempts += 1

    return best_result