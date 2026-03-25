import streamlit as st
from main import enhance_prompt

st.set_page_config(page_title="PromptPal", page_icon="🔮")

st.title("PromptPal : Prompt Enhancer for LLMs")
st.markdown("Enter a rough prompt and get an optimized version suitable for ChatGPT or other LLMs.")

user_input = st.text_area(" Your rough prompt", height=150)

if st.button("Enhance"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Enhancing..."):
            try:
                result = enhance_prompt(user_input)
                st.success("Here's your enhanced prompt:")
                st.text_area("Enhanced Prompt", value=result, height = 200, disabled=True)

            except Exception as e:
                st.error(f"Error: {e}")
