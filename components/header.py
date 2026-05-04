import streamlit as st


def render_header():
    st.markdown('<div class="page-title">PromptPal</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Multi-step LLM pipeline that classifies, enhances, and evaluates your prompts.</div>',
        unsafe_allow_html=True
    )
    st.markdown('<hr class="divider">', unsafe_allow_html=True)