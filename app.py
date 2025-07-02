import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

# Page config
st.set_page_config(
    page_title="scribe.",
    page_icon="📝",
    layout="centered",
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

    html, body, [class*="css"], .main, .stApp, .block-container {
        background-color: #0e1117;
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace !important;
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
        background-color: #2a2a2a; /* Slight grey background */
        border: 1px solid #444;
        border-radius: 8px;
        margin-top: 1em;
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
    .review-icon {
        font-size: 20px;
        margin-top: 2px;
    }
    .review-text {
        flex: 1;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered">', unsafe_allow_html=True)
st.title("scribe.")
st.markdown("<h3 style='margin-top: 0;'>Real Feedback. Word for Word.</h3>", unsafe_allow_html=True)
st.markdown("""
<p>Feedback’s messy.
Scribe helps you ask sharp questions and surfaces the most relevant answers from noisy reviews.<br>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Use CPU explicitly and avoid meta tensor issues
# Force CPU for Torch and avoid meta tensor errors
os.environ["CUDA_VISIBLE_DEVICES"] = ""
embedder = SentenceTransformer('all-MiniLM-L6-v2')
mode = st.radio("Choose an option:", ["Review Sample", "Try it Yourself"], horizontal=True)

if mode == "Review Sample":
    sample_data = pd.read_csv('food_delivery_apps.csv')
    user_question = st.text_input("Ask your question about the sample reviews")
else:
    uploaded_file = st.file_uploader("Upload a CSV file with a 'review_text' column", type=["csv"])
    user_question = st.text_input("Enter your question")
    if uploaded_file:
        try:
            sample_data = pd.read_csv(uploaded_file)
            if 'content' not in sample_data.columns:
                st.error("CSV must contain a 'content' column.")
                st.stop()
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.stop()
    else:
        sample_data = None

# --- Submit and Local Embedding Logic ---
if st.button("Ask the Crowd!") and sample_data is not None and user_question:
    try:
        reviews = sample_data["content"].dropna().astype(str).tolist()
        review_embeddings = embedder.encode(reviews, convert_to_tensor=True)
        question_embedding = embedder.encode(user_question, convert_to_tensor=True)

        # Compute cosine similarities
        cosine_scores = util.cos_sim(question_embedding, review_embeddings)[0]
        top_results = torch.topk(cosine_scores, k=5)

        st.success("🌟 Top Relevant Reviews")
        for score, idx in zip(top_results.values, top_results.indices):
            st.markdown(f"- {reviews[idx]}")
    except Exception as e:
        st.error(f"Error: {e}")

if mode == "Review Sample":
    sample_data = pd.read_csv('food_delivery_apps.csv')
    st.markdown(" All Sample reviews", unsafe_allow_html=True)
    review_html =""
    # Scrollable review list
    for review in sample_data["content"]:
        st.markdown(review, unsafe_allow_html=True)
