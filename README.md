# Text Sentiment Analyzer with Streamlit

This project provides a simple web application for performing sentiment analysis on text using a pre-trained model from the Hugging Face `transformers` library.

## Features
- Analyze the sentiment (Positive, Negative, Neutral) of any given text.
- Displays the confidence score of the sentiment.
- Easy-to-use Streamlit interface.

## Getting Started

### Prerequisites
Make sure you have Python 3.7+ installed.

### Installation
1. Clone this repository (if applicable) or create a new project directory.
2. Create a `requirements.txt` file with the following content:
streamlit transformers

3. Install the required Python packages:
```bash
pip install -r requirements.txt
Running the Application
Save the Streamlit application code into a Python file, e.g., app.py. (The code was provided in a previous output.)
Run the application from your terminal:
If you are running locally:

streamlit run app.py
If you are running in Google Colab (to expose the app via localtunnel):

!streamlit run app.py & npx localtunnel --port 8501
(You might need to install npx if it's not already available in your environment, e.g., npm install -g npx or apt-get install npm then npm install -g npx if in a Linux-like environment.)

Once the application is running, open your web browser and navigate to the provided URL (usually http://localhost:8501 for local or the localtunnel URL for Colab).

Usage
Enter the text you want to analyze into the text area.
Click the "Analyze Sentiment" button.
The application will display the predicted sentiment (Positive, Negative, or Neutral) and its confidence score.
Example
Input Text: "I love learning AI!"

Output: Sentiment: POSITIVE Confidence: 0.99 This text expresses positive sentiment! ```


