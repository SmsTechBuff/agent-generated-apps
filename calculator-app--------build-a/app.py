import gradio as gr

def calculator(num1, operator, num2):
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
            return num1 / num2
        else:
            return "Error: Invalid operator"
    except ValueError:
        return "Error: Invalid input"

def update_output(num1, operator, num2, output):
    if output is not None:
        return output
    else:
        return ""

demo = gr.Blocks()

with demo:
    gr.Header("Calculator App")
    
    num1 = gr.Number(label="Number 1")
    operator = gr.Radio(
        choices=["+", "-", "*", "/"],
        label="Operator",
        type="value",
    )
    num2 = gr.Number(label="Number 2")
    
    output = gr.Number(label="Output")
    
    gr.Button("Calculate").click(
        calculator,
        inputs=[num1, operator, num2],
        outputs=output,
    )
    
    gr.Button("Clear").click(
        update_output,
        inputs=[num1, operator, num2, output],
        outputs=output,
        queue=False,
    )

if __name__ == "__main__":
    demo.launch()