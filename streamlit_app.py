import streamlit as st
from transformers import pipeline

# Load the pre-trained sentiment analysis model
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

analyzer = load_model()

st.title("Text Sentiment Analyzer")

user_input = st.text_area("Enter text for sentiment analysis:", "I love learning AI!")

if st.button("Analyze Sentiment"):
    if user_input:
        result = analyzer(user_input)
        label = result[0]['label']
        score = result[0]['score']
        
        st.write(f"**Sentiment:** {label}")
        st.write(f"**Confidence:** {score:.2f}")
        
        if label == 'POSITIVE':
            st.success("This text expresses positive sentiment!")
        elif label == 'NEGATIVE':
            st.error("This text expresses negative sentiment.")
        else:
            st.info("This text expresses neutral sentiment.")
    else:
        st.warning("Please enter some text to analyze.")
