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
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operator"
    except ValueError:
        return "Error: Invalid input"

def update_output(num1, operator, num2, output):
    if output == "":
        return ""
    else:
        return output

demo = gr.Blocks()

with demo:
    gr.Markdown("# Calculator App")
    num1 = gr.Number(label="Number 1")
    operator = gr.Dropdown(label="Operator", choices=["+", "-", "*", "/"])
    num2 = gr.Number(label="Number 2")
    output = gr.Number(label="Output")
    equals = gr.Button("Calculate")
    clear = gr.Button("Clear")

    equals.click(
        calculate,
        inputs=[num1, operator, num2],
        outputs=output,
    )

    clear.click(
        update_output,
        inputs=[num1, operator, num2, output],
        outputs=output,
        queue=False,
    )

    clear.click(
        lambda: "",
        None,
        num1,
        queue=False,
    )

    clear.click(
        lambda: "",
        None,
        operator,
        queue=False,
    )

    clear.click(
        lambda: "",
        None,
        num2,
        queue=False,
    )

if __name__ == "__main__":
    demo.launch()