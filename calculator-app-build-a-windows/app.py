import gradio as gr

def calculator_interface(math_expression):
    try:
        result = eval(math_expression)
        return str(result)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return str(e)

def clear_input(math_expression):
    return ""

demo = gr.Blocks()

with demo:
    math_expression = gr.Textbox(label="Calculator")
    result = gr.Textbox(label="Result")

    button_7 = gr.Button("7")
    button_8 = gr.Button("8")
    button_9 = gr.Button("/")
    button_div = gr.Button("/")

    button_4 = gr.Button("4")
    button_5 = gr.Button("5")
    button_6 = gr.Button("*")
    button_mul = gr.Button("*")

    button_1 = gr.Button("1")
    button_2 = gr.Button("2")
    button_3 = gr.Button("-")
    button_sub = gr.Button("-")

    button_0 = gr.Button("0")
    button_dot = gr.Button(".")
    button_equal = gr.Button("=")
    button_add = gr.Button("+")

    button_c = gr.Button("C")

    button_7.click(
        lambda: math_expression.update(value=math_expression.value + "7"),
        inputs=None,
        outputs=[math_expression],
    )

    button_8.click(
        lambda: math_expression.update(value=math_expression.value + "8"),
        inputs=None,
        outputs=[math_expression],
    )

    button_9.click(
        lambda: math_expression.update(value=math_expression.value + "9"),
        inputs=None,
        outputs=[math_expression],
    )

    button_4.click(
        lambda: math_expression.update(value=math_expression.value + "4"),
        inputs=None,
        outputs=[math_expression],
    )

    button_5.click(
        lambda: math_expression.update(value=math_expression.value + "5"),
        inputs=None,
        outputs=[math_expression],
    )

    button_6.click(
        lambda: math_expression.update(value=math_expression.value + "6"),
        inputs=None,
        outputs=[math_expression],
    )

    button_1.click(
        lambda: math_expression.update(value=math_expression.value + "1"),
        inputs=None,
        outputs=[math_expression],
    )

    button_2.click(
        lambda: math_expression.update(value=math_expression.value + "2"),
        inputs=None,
        outputs=[math_expression],
    )

    button_3.click(
        lambda: math_expression.update(value=math_expression.value + "3"),
        inputs=None,
        outputs=[math_expression],
    )

    button_0.click(
        lambda: math_expression.update(value=math_expression.value + "0"),
        inputs=None,
        outputs=[math_expression],
    )

    button_dot.click(
        lambda: math_expression.update(value=math_expression.value + "."),
        inputs=None,
        outputs=[math_expression],
    )

    button_add.click(
        lambda: math_expression.update(value=math_expression.value + "+"),
        inputs=None,
        outputs=[math_expression],
    )

    button_sub.click(
        lambda: math_expression.update(value=math_expression.value + "-"),
        inputs=None,
        outputs=[math_expression],
    )

    button_mul.click(
        lambda: math_expression.update(value=math_expression.value + "*"),
        inputs=None,
        outputs=[math_expression],
    )

    button_div.click(
        lambda: math_expression.update(value=math_expression.value + "/"),
        inputs=None,
        outputs=[math_expression],
    )

    button_equal.click(
        calculator_interface,
        inputs=[math_expression],
        outputs=[result],
    )

    button_c.click(
        clear_input,
        inputs=[math_expression],
        outputs=[math_expression, result],
    )

    gr.Columns([button_7, button_8, button_9, button_div])
    gr.Columns([button_4, button_5, button_6, button_mul])
    gr.Columns([button_1, button_2, button_3, button_sub])
    gr.Columns([button_0, button_dot, button_equal, button_add])
    gr.Columns([button_c])

if __name__ == "__main__":
    demo.launch()