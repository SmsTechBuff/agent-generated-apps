import gradio as gr

def calculate(num1, operator, num2):
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
            return num1 / num2
        else:
            return "Error: Invalid operator"
    except Exception as e:
        return str(e)

def update_num1(num1, digit):
    if num1 == "" or num1 == 0:
        return digit
    else:
        return str(num1) + str(digit)

def update_num2(num2, digit):
    if num2 == "" or num2 == 0:
        return digit
    else:
        return str(num2) + str(digit)

def clear(num1, num2, operator, result):
    return "", "", "", ""

demo = gr.Blocks()

with demo:
    gr.Markdown("# Calculator App")
    num1 = gr.Textbox(label="Number 1", placeholder="0")
    operator = gr.Dropdown(["+", "-", "*", "/"], label="Operator")
    num2 = gr.Textbox(label="Number 2", placeholder="0")
    result = gr.Textbox(label="Result")

    gr.Button("7").click(
        lambda num1: update_num1(num1, "7"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("8").click(
        lambda num1: update_num1(num1, "8"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("9").click(
        lambda num1: update_num1(num1, "9"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("/").click(
        lambda: "/",
        inputs=None,
        outputs=operator,
    )

    gr.Button("4").click(
        lambda num1: update_num1(num1, "4"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("5").click(
        lambda num1: update_num1(num1, "5"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("6").click(
        lambda num1: update_num1(num1, "6"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("*").click(
        lambda: "*",
        inputs=None,
        outputs=operator,
    )

    gr.Button("1").click(
        lambda num1: update_num1(num1, "1"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("2").click(
        lambda num1: update_num1(num1, "2"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("3").click(
        lambda num1: update_num1(num1, "3"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("-").click(
        lambda: "-",
        inputs=None,
        outputs=operator,
    )

    gr.Button("0").click(
        lambda num1: update_num1(num1, "0"),
        inputs=num1,
        outputs=num1,
    )
    gr.Button(".").click(
        lambda num1: update_num1(num1, "."),
        inputs=num1,
        outputs=num1,
    )
    gr.Button("=").click(
        lambda num1, operator, num2: calculate(float(num1), operator, float(num2)),
        inputs=[num1, operator, num2],
        outputs=result,
    )
    gr.Button("+").click(
        lambda: "+",
        inputs=None,
        outputs=operator,
    )

    gr.Button("Clear").click(
        clear,
        inputs=[num1, num2, operator, result],
        outputs=[num1, num2, operator, result],
    )

    gr.Grid(
        [
            [gr.Button("7"), gr.Button("8"), gr.Button("9"), gr.Button("/")],
            [gr.Button("4"), gr.Button("5"), gr.Button("6"), gr.Button("*")],
            [gr.Button("1"), gr.Button("2"), gr.Button("3"), gr.Button("-")],
            [gr.Button("0"), gr.Button("."), gr.Button("="), gr.Button("+")],
            [gr.Button("Clear")],
        ]
    )
    gr.Grid(
        [
            [num1, operator, num2, result],
        ]
    )

if __name__ == "__main__":
    demo.launch()