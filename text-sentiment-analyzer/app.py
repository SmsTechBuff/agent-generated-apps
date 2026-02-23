import gradio as gr
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def sentiment_analysis(text):
    if not text:
        return "Please enter some text"
    try:
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        compound_score = sentiment['compound']
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        return f"An error occurred: {str(e)}"

demo = gr.Interface(
    fn=sentiment_analysis,
    inputs="text",
    outputs="text",
    title="Sentiment Analysis",
    description="Enter some text to analyze its sentiment",
)

if __name__ == "__main__":
    demo.launch()