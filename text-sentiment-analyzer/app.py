import gradio as gr
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.

    Args:
    text (str): The text to analyze.

    Returns:
    dict: A dictionary containing the sentiment analysis results.
    """
    if not text:
        return {"Sentiment": "Unknown", "Positive": 0, "Negative": 0, "Neutral": 0}

    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    if sentiment_scores['compound'] > 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "Sentiment": sentiment,
        "Positive": sentiment_scores['pos'],
        "Negative": sentiment_scores['neg'],
        "Neutral": sentiment_scores['neu']
    }

demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(label="Text to analyze"),
    outputs=[
        gr.Label(label="Sentiment"),
        gr.Number(label="Positive sentiment score"),
        gr.Number(label="Negative sentiment score"),
        gr.Number(label="Neutral sentiment score")
    ],
    title="Text Sentiment Analyzer",
    description="Analyze the sentiment of a given text."
)

if __name__ == "__main__":
    demo.launch()