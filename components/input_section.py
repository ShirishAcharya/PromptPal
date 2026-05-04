import streamlit as st


def render_input() -> tuple[str, bool]:
    col_input, _ = st.columns([2, 1])

    with col_input:
        st.markdown('<div class="section-label">Your Prompt</div>', unsafe_allow_html=True)
        user_input = st.text_area(
            label="",
            placeholder="Write a rough or vague prompt and let PromptPal improve it...",
            height=160,
            label_visibility="collapsed"
        )
        run = st.button("Run Workflow")

    return user_input, run