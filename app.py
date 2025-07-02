import streamlit as st
from utils.styles import apply_dark_theme
from utils.model import load_embedder, find_top_reviews
from utils.data import load_sample_data, load_uploaded_data

page = st.query_params.get_all("page") 
apply_dark_theme()
print(page)
if page == "home" or not page: 
    st.query_params.clear()
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.markdown('<h1 class="stTitle">scribe.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="stSubheader">Real Feedback. Word for Word.</p>', unsafe_allow_html=True)

    # st.markdown("""
    # <p>Feedback’s messy.<br>
    # Scribe helps you surface the most relevant answers from noisy reviews.<br>
    # """, unsafe_allow_html=True)
    # st.markdown('</div>', unsafe_allow_html=True)

    sample_data = load_sample_data()
    preview_reviews = sample_data["content"].dropna().astype(str).tolist()[:10]

    user_question = st.text_input("Ask a question. Get straight to what matters. ")

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


    col1, col2 = st.columns([5, 1.5],gap="small")

    with col1:
        st.markdown("", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stDownloadButton">', unsafe_allow_html=True)
        if st.button("Use your own data!"):
            st.query_params.from_dict({"page": "upload"})
            st.rerun()
        
    with st.expander("📖 View All Sample Reviews", expanded=True):
        st.markdown('<div class="stDownloadButton">', unsafe_allow_html=True)
        st.download_button(
            label="📂 Explore Full Sample",
            data=sample_data.to_csv(index=False),
            file_name="sample_reviews.csv",
            mime="text/csv",
            use_container_width=True
        )
        for review in preview_reviews:
            cleaned_review = str(review).replace("\n", " ").strip()
            st.markdown(f"""
            <div class='review-line'>
                <div class='review-icon'>👤</div>
                <div class='review-text'>{cleaned_review}</div>
            </div>
            """, unsafe_allow_html=True)
            
else:
    import upload
    upload.app()
