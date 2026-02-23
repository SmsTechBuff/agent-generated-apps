import gradio as gr
from collections import Counter
import re

def word_frequency(text):
    # Remove punctuation and convert to lower case
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    frequency = Counter(words)
    
    # Create a list of tuples with the word and its frequency
    frequency_list = [(word, freq) for word, freq in frequency.items()]
    
    # Sort the list in descending order of frequency
    frequency_list.sort(key=lambda x: x[1], reverse=True)
    
    return frequency_list

demo = gr.Interface(
    fn=word_frequency,
    inputs="text",
    outputs="json",
    title="Word Frequency Counter",
    description="Enter a text to get the frequency of each word",
    examples=[
        ["This is a test. This test is only a test."],
        ["The quick brown fox jumps over the lazy dog."],
        ["The sun was shining brightly in the clear blue sky."]
    ]
)

if __name__ == "__main__":
    demo.launch()