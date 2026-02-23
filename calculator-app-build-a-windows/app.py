import gradio as gr

def calculator(num1, operator, num2):
    try:
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
    except Exception as e:
        return str(e)

demo = gr.Blocks()

with demo:
    gr.Markdown("# Calculator App")
    num1 = gr.Number(label="Number 1")
    operator = gr.Dropdown(label="Operator", choices=["+", "-", "*", "/"])
    num2 = gr.Number(label="Number 2")
    result = gr.Number(label="Result")

    gr.Button("Calculate").click(
        calculator,
        inputs=[num1, operator, num2],
        outputs=result,
    )

    gr.Button("Clear").click(
        lambda: [0, None, 0, None],
        inputs=None,
        outputs=[num1, operator, num2, result],
    )

    gr.Button("7").click(
        lambda: 7,
        inputs=None,
        outputs=num1,
    )
    gr.Button("8").click(
        lambda: 8,
        inputs=None,
        outputs=num1,
    )
    gr.Button("9").click(
        lambda: 9,
        inputs=None,
        outputs=num1,
    )
    gr.Button("/").click(
        lambda: "/",
        inputs=None,
        outputs=operator,
    )

    gr.Button("4").click(
        lambda: 4,
        inputs=None,
        outputs=num1,
    )
    gr.Button("5").click(
        lambda: 5,
        inputs=None,
        outputs=num1,
    )
    gr.Button("6").click(
        lambda: 6,
        inputs=None,
        outputs=num1,
    )
    gr.Button("*").click(
        lambda: "*",
        inputs=None,
        outputs=operator,
    )

    gr.Button("1").click(
        lambda: 1,
        inputs=None,
        outputs=num1,
    )
    gr.Button("2").click(
        lambda: 2,
        inputs=None,
        outputs=num1,
    )
    gr.Button("3").click(
        lambda: 3,
        inputs=None,
        outputs=num1,
    )
    gr.Button("-").click(
        lambda: "-",
        inputs=None,
        outputs=operator,
    )

    gr.Button("0").click(
        lambda: 0,
        inputs=None,
        outputs=num1,
    )
    gr.Button(".").click(
        lambda: ".",
        inputs=None,
        outputs=num1,
    )
    gr.Button("=").click(
        lambda: "=",
        inputs=None,
        outputs=None,
    )
    gr.Button("+").click(
        lambda: "+",
        inputs=None,
        outputs=operator,
    )

if __name__ == "__main__":
    demo.launch()