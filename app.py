import streamlit as st
from workflow.prompt_workflow import run_prompt_workflow

st.set_page_config(page_title="PromptPal")

st.title("PromptPal – LLM Workflow Engine")
st.markdown("Transform raw prompts through an agentic multi-step LLM pipeline.")

user_input = st.text_area("Enter your rough prompt", height=150)

if st.button("Run Workflow"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Running workflow..."):
            try:
                result = run_prompt_workflow(user_input)

                intent = result["intent"].get("intent", "unknown")
                enhanced = result["output"].get("enhanced_prompt", "")
                score = result["evaluation"].get("score", "N/A")
                feedback = result["evaluation"].get("feedback", "")

                st.success("Workflow Completed")

                st.markdown(f"### Detected Intent: `{intent}`")
                st.markdown(f"### Prompt Quality Score: `{score}/10`")

                st.text_area("Enhanced Prompt", value=enhanced, height=200)

                with st.expander("Workflow Breakdown"):
                    st.json(result)

                with st.expander("Evaluation Feedback"):
                    st.write(feedback)

            except Exception as e:
                st.error(f"Error: {e}")