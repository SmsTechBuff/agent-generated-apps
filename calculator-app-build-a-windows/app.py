import gradio as gr

def calculate(num1, operator, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Division by zero"
            else:
                return num1 / num2
        else:
            return "Invalid operator"
    except ValueError:
        return "Invalid input"

def button_click(num1, operator, num2, button):
    try:
        if button == "C":
            return "", "", ""
        elif button == "=":
            return num1, operator, str(calculate(num1, operator, num2))
        elif button in ["+", "-", "*", "/"]:
            return num1, button, num2
        elif button.isdigit():
            if num1 == "":
                return button, operator, num2
            elif operator == "":
                return num1 + button, operator, num2
            else:
                return num1, operator, num2 + button
        else:
            return num1, operator, num2
    except Exception as e:
        return num1, operator, num2

demo = gr.Blocks()

with demo:
    num1 = gr.Textbox(label="Number 1", placeholder="Enter number 1")
    num2 = gr.Textbox(label="Number 2", placeholder="Enter number 2")
    operator = gr.Textbox(label="Operator", placeholder="Operator")

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", "C", "=", "+"],
    ]

    for row in buttons:
        with gr.Row():
            for button in row:
                gr.Button(button).click(
                    button_click,
                    inputs=[num1, operator, num2, gr.Button(button)],
                    outputs=[num1, operator, num2],
                    queue=False,
                )

if __name__ == "__main__":
    demo.launch()