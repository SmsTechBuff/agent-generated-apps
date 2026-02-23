import gradio as gr
import matplotlib.pyplot as plt

def plot_graph(x, y):
    try:
        # Check if input lists have 5 elements each
        if len(x) != 5 or len(y) != 5:
            return "Error: Input lists must have 5 elements each."
        
        # Check if all input values are numbers
        if not all(isinstance(i, (int, float)) for i in x) or not all(isinstance(i, (int, float)) for i in y):
            return "Error: All input values must be numbers."
        
        # Create the plot
        plt.plot(x, y, marker='o')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Graph Plot')
        plt.grid(True)
        
        # Return the plot as an image
        return plt.show()
    except Exception as e:
        return f"An error occurred: {str(e)}"

demo = gr.Interface(
    plot_graph,
    [
        gr.Number(label="X1", value=1),
        gr.Number(label="X2", value=2),
        gr.Number(label="X3", value=3),
        gr.Number(label="X4", value=4),
        gr.Number(label="X5", value=5),
        gr.Number(label="Y1", value=1),
        gr.Number(label="Y2", value=2),
        gr.Number(label="Y3", value=3),
        gr.Number(label="Y4", value=4),
        gr.Number(label="Y5", value=5),
    ],
    "plot",
    title="Graph Plotting App",
    description="Enter 5 X values and 5 Y values to plot a graph.",
)

if __name__ == "__main__":
    demo.launch()