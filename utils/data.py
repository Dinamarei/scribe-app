import pandas as pd
import streamlit as st

def load_sample_data():
    return pd.read_csv('food_delivery_apps.csv')

def load_uploaded_data(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        if 'content' not in df.columns:
            st.error("CSV must contain a 'content' column.")
            st.stop()
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()
