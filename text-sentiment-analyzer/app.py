import gradio as gr
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download required NLTK data if not already downloaded
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: The sentiment of the text (positive, negative, or neutral).
    """
    if not text:
        return "Please enter some text to analyze."

    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    if sentiment_scores['compound'] > 0.05:
        return "Positive"
    elif sentiment_scores['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"

demo = gr.Interface(
    analyze_sentiment,
    gr.Textbox(label="Text to analyze"),
    gr.Label(label="Sentiment"),
    title="Text Sentiment Analyzer",
    description="Analyze the sentiment of a piece of text.",
)

if __name__ == "__main__":
    demo.launch()