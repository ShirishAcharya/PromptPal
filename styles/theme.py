def load_css() -> str:
    return """
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans', sans-serif;
    }

    .stApp {
        background-color: #0e0e0e;
        color: #e8e8e8;
    }

    .block-container {
        padding: 3rem 4rem;
        max-width: 1100px;
    }

    h1, h2, h3 {
        font-family: 'IBM Plex Mono', monospace !important;
        letter-spacing: -0.5px;
    }

    .page-title {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 2rem;
        font-weight: 500;
        color: #e8e8e8;
        margin-bottom: 0.15rem;
    }

    .page-subtitle {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.95rem;
        color: #666;
        margin-bottom: 2.5rem;
    }

    .divider {
        border: none;
        border-top: 1px solid #1f1f1f;
        margin: 2rem 0;
    }

    .stTextArea textarea {
        background-color: #141414 !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 6px !important;
        color: #e8e8e8 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.875rem !important;
        line-height: 1.6 !important;
        padding: 1rem !important;
        transition: border-color 0.2s ease;
    }

    .stTextArea textarea:focus {
        border-color: #c8f542 !important;
        box-shadow: none !important;
    }

    .stButton > button {
        background-color: #c8f542 !important;
        color: #0e0e0e !important;
        border: none !important;
        border-radius: 4px !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px !important;
        padding: 0.6rem 1.8rem !important;
        cursor: pointer !important;
        transition: opacity 0.2s ease !important;
    }

    .stButton > button:hover {
        opacity: 0.85 !important;
    }

    .metric-card {
        background-color: #141414;
        border: 1px solid #1f1f1f;
        border-radius: 6px;
        padding: 1.2rem 1.4rem;
    }

    .metric-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.7rem;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.4rem;
    }

    .metric-value {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.6rem;
        font-weight: 500;
        color: #c8f542;
    }

    .metric-value-text {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #e8e8e8;
    }

    .result-box {
        background-color: #141414;
        border: 1px solid #1f1f1f;
        border-left: 3px solid #c8f542;
        border-radius: 6px;
        padding: 1.4rem 1.6rem;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.85rem;
        line-height: 1.7;
        color: #d0d0d0;
        white-space: pre-wrap;
    }

    .feedback-box {
        background-color: #141414;
        border: 1px solid #1f1f1f;
        border-radius: 6px;
        padding: 1.4rem 1.6rem;
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.875rem;
        line-height: 1.7;
        color: #aaa;
    }

    .section-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #444;
        margin-bottom: 0.75rem;
    }

    .streamlit-expanderHeader {
        background-color: #141414 !important;
        border: 1px solid #1f1f1f !important;
        border-radius: 6px !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.8rem !important;
        color: #666 !important;
    }

    .streamlit-expanderContent {
        background-color: #141414 !important;
        border: 1px solid #1f1f1f !important;
        border-top: none !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""