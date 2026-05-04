import streamlit as st


def render_metrics(intent: str, score, enhanced: str):
    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Detected Intent</div>
                <div class="metric-value-text">{intent.title()}</div>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Quality Score</div>
                <div class="metric-value">{score}<span style="font-size:0.9rem; color:#555;">/10</span></div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        word_count = len(enhanced.split()) if enhanced else 0
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Enhanced Length</div>
                <div class="metric-value">{word_count}<span style="font-size:0.9rem; color:#555;"> words</span></div>
            </div>
        """, unsafe_allow_html=True)