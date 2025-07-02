import streamlit as st

def apply_dark_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

        html, body, [class*="css"], .main, .stApp, .block-container {
            background-color: #0e1117;
            color: #ffffff;
            font-family: 'JetBrains Mono', monospace !important;
        }
        
        .top-right-button {
    position: fixed;
    top: 10px;
    right: 10px;
    background-color: rgba(0, 128, 0, 0.7); /* green with 70% opacity */
    color: white !important;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
    z-index: 1000;
    text-decoration: none;
}
        h1, h2, h3, p, label, .uploadedFileName, .stTextInput>div>div>input, .stButton>button {
            color: #ffffff !important;
        }
        .stTextInput>div>div>input {
            background-color: #1c1e26 !important;
            border-color: #3c3f4a;
        }
        .stButton>button {
            background-color: #262730;
            border: 1px solid #ffffff33;
        }
          .stTitle {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 0px;
        text-align: center;
        width: 100%;
        }
        .stSubheader {
            font-size: 20px;
            color: #bbbbbb;
            margin-top: 0;
            margin-bottom: 40px;
            text-align: center;
            width: 100%;
        }

        .centered {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            margin-top: 20px;
        }
        .scroll-box {
            max-height: 320px;
            overflow-y: auto;
            padding: 16px;
            background-color: #2a2a2a;
            border: 1px solid #444;
            border-radius: 8px;
            margin-top: 1em;
        }
        
         .results-container {
        max-width: 700px;
        margin-top: 30px;
        padding: 20px 30px;
        background-color: #1e1e28;
        border-radius: 12px;
        box-shadow: 0 4px 24px rgb(0 0 0 / 0.6);
        color: #e0e0e0;
        font-size: 16px;
        line-height: 1.6;
    }
    .results-container ul {
        padding-left: 20px;
    }
    .results-container li {
        margin-bottom: 12px;
    }
    .right-align {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 20px;
    }

        .review-line {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 16px;
            background-color: #1c1e26;
            padding: 12px 14px;
            border-radius: 8px;
            border: 1px solid #333;
            font-size: 14px;
        }
        .relevant-review-line {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 16px;
            background-color: #06402b;
            padding: 12px 14px;
            border-radius: 8px;
            border: 1px solid #333;
            font-size: 14px;
        }
        .review-icon {
            font-size: 20px;
            margin-top: 2px;
        }
        .review-text {
        flex: 1;
        line-height: 1.6;
        white-space: pre-wrap;
        word-break: break-word;
        overflow-wrap: break-word;
        max-width: 100%;
    }
    .stDownloadButton button {
      font-size: 9px !important;
        padding: 6px 10px !important;
        width: 100% !important;
        background-color: #262730 !important;
        color: white !important;
        border-radius: 6px !important;
        border: 1px solid #ffffff33 !important;

        </style>
    """, unsafe_allow_html=True)
