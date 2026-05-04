import streamlit as st


def render_results(enhanced: str, feedback: str, full_result: dict):
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-label">Enhanced Prompt</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-box">{enhanced}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if feedback:
        st.markdown('<div class="section-label">Evaluation Feedback</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="feedback-box">{feedback}</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("Full workflow breakdown"):
        st.json(full_result)