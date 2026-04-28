from workflow.prompt_workflow import run_prompt_workflow
import json

if __name__ == "__main__":
    print("PromptPal Workflow Engine")
    user_input = input("Enter your prompt: ")

    result = run_prompt_workflow(user_input)

    print(json.dumps(result, indent=2))