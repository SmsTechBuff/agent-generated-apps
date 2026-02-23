import gradio as gr

def decommission_app(input_text):
    if not input_text:
        return "Please provide a reason for decommissioning the app."
    return f"App decommissioned due to: {input_text}"

demo = gr.Interface(
    fn=decommission_app,
    inputs="text",
    outputs="text",
    title="Decommission App",
    description="Enter a reason to decommission the Build-a-Tic-Tac-Toe-Game-With app",
)

if __name__ == "__main__":
    demo.launch()