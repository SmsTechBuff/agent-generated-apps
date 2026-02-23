import gradio as gr
from collections import Counter
import re

def word_count(text):
    # Remove punctuation and convert to lower case
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split text into words
    words = text.split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Create a list of tuples with word and count
    result = [(word, count) for word, count in word_counts.items()]
    
    return result

def main(text):
    if not text:
        return "Please enter a sentence or paragraph."
    
    try:
        result = word_count(text)
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"

demo = gr.Interface(
    main,
    gr.Textbox(label="Enter a sentence or paragraph"),
    gr.JSON(label="Word counts"),
    title="Word Count Analyzer",
    description="Enter a sentence or paragraph to analyze and calculate the word counts."
)

if __name__ == "__main__":
    demo.launch()