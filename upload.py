import streamlit as st
from utils.styles import apply_dark_theme
from utils.model import load_embedder, find_top_reviews
from utils.data import load_uploaded_data
import os

def app():
    page = st.query_params["page"]
    
    if page =="upload":
        apply_dark_theme()
        st.query_params.clear()
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.title("Try Your Own Data")
        st.markdown("Upload your CSV file with a `content` column and ask your question below.", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        embedder = load_embedder()

        uploaded_file = st.file_uploader("Upload a CSV file with a 'content' column", type=["csv"])
        user_question = st.text_input("Enter your question")

        if uploaded_file:
            sample_data = load_uploaded_data(uploaded_file)
        else:
            sample_data = None

        if st.button("Gather Wisdom!") and sample_data is not None and user_question:
            try:
                embedder = load_embedder() 
                top_reviews = find_top_reviews(sample_data["content"].dropna().astype(str).tolist(), user_question, embedder)
                st.markdown('<p class="stTitle">⭐️ Top Relevant Reviews ⭐️</p><br>', unsafe_allow_html=True)
                
                for review in top_reviews:
                    cleaned_review = str(review).replace("\n", " ").strip()
                    st.markdown(f"""
                    <div class='relevant-review-line'>
                        <div class='review-icon'>👤</div>
                        <div class='review-text'>{cleaned_review}</div>
                    </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                print(e)
                st.error("Sorry this service is not available now. Please try again later.")

        col1, col2 = st.columns([4, 1],gap="small")

        with col1:
            st.markdown("", unsafe_allow_html=True)

        with col2:
            if st.button("Explore Demo."):
                st.query_params.from_dict({"page": "home"})
                st.rerun()
    else:
        import app
        