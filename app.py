import streamlit as st
from styles.theme import load_css
from components.header import render_header
from components.input_section import render_input
from components.metrics import render_metrics
from components.results import render_results
from workflow.prompt_workflow import run_prompt_workflow

st.set_page_config(
    page_title="PromptPal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(load_css(), unsafe_allow_html=True)

render_header()

user_input, run = render_input()

if run:
    if not user_input.strip():
        st.warning("Please enter a prompt before running.")
    else:
        with st.spinner("Running pipeline..."):
            try:
                result = run_prompt_workflow(user_input)

                intent = result["intent"].get("intent", "unknown")
                enhanced = result["output"].get("enhanced_prompt") or result["output"].get("raw", "")
                score = result["evaluation"].get("score", "N/A")
                feedback = result["evaluation"].get("feedback", "")

                st.markdown('<hr class="divider">', unsafe_allow_html=True)
                render_metrics(intent, score, enhanced)
                render_results(enhanced, feedback, result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")