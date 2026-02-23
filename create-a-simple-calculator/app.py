import gradio as gr

def calculate(num1, operator, num2):
    try:
        if operator == "Add":
            return num1 + num2
        elif operator == "Subtract":
            return num1 - num2
        elif operator == "Multiply":
            return num1 * num2
        elif operator == "Divide":
            if num2 == 0:
                return "Error: Division by zero"
            else:
                return num1 / num2
    except Exception as e:
        return str(e)

demo = gr.Interface(
    calculate,
    [
        gr.Number(label="Number 1"),
        gr.Radio(
            choices=["Add", "Subtract", "Multiply", "Divide"],
            type="value",
            label="Operator",
        ),
        gr.Number(label="Number 2"),
    ],
    gr.Textbox(label="Result"),
)

if __name__ == "__main__":
    demo.launch()