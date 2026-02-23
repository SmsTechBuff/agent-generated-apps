import gradio as gr
from collections import Counter
import matplotlib.pyplot as plt
import re
from io import BytesIO
import base64

def word_frequency(text):
    # Remove punctuation and convert to lower case
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    
    # Count word frequency
    word_freq = Counter(words)
    
    # Get the most common words
    most_common = word_freq.most_common(10)
    
    # Create a plot of the most frequent words
    plt.bar([word for word, freq in most_common], [freq for word, freq in most_common])
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Most Frequent Words')
    plt.xticks(rotation=90)
    
    # Save the plot to a bytes buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Clear the plot for the next iteration
    plt.clf()
    
    # Return the word frequency and the plot
    return dict(word_freq), img

demo = gr.Interface(
    fn=word_frequency,
    inputs=gr.Textbox(label="Text"),
    outputs=[gr.JSON(label="Word Frequency"), gr.Image(label="Most Frequent Words")],
    title="Word Frequency Analyzer",
    description="Enter a text to analyze the word frequency and view the most frequent words."
)

if __name__ == "__main__":
    demo.launch()