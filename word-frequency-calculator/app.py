import gradio as gr
from collections import Counter
import re

def calculate_word_frequency(text):
    # Remove punctuation and convert to lower case
    text = re.sub(r'[^\w\s]', '', text).lower()
    # Split text into words
    words = text.split()
    # Count word frequency
    frequency = Counter(words)
    # Sort frequency by value in descending order
    sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    return sorted_frequency

demo = gr.Interface(
    fn=calculate_word_frequency,
    inputs=gr.Textbox(label="Text"),
    outputs=gr.JSON(label="Word Frequency"),
    title="Word Frequency Calculator",
    description="Calculate the frequency of each word in a given text.",
)

if __name__ == "__main__":
    demo.launch()