import gradio as gr

def calculate(expression):
    try:
        return str(eval(expression))
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return str(e)

def clear_textbox():
    return ""

def update_textbox(textbox_value, button_value):
    if button_value == "=":
        return calculate(textbox_value)
    elif button_value == "C":
        return clear_textbox()
    else:
        return textbox_value + button_value

demo = gr.Blocks()

with demo:
    textbox = gr.Textbox(label="Calculator", placeholder="Enter expression")

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
    button_eq = gr.Button("=")
    button_add = gr.Button("+")

    button_c = gr.Button("C")

    button_7.click(lambda _, textbox_value: update_textbox(textbox_value, "7"), inputs=[textbox], outputs=[textbox])
    button_8.click(lambda _, textbox_value: update_textbox(textbox_value, "8"), inputs=[textbox], outputs=[textbox])
    button_9.click(lambda _, textbox_value: update_textbox(textbox_value, "9"), inputs=[textbox], outputs=[textbox])
    button_div.click(lambda _, textbox_value: update_textbox(textbox_value, "/"), inputs=[textbox], outputs=[textbox])

    button_4.click(lambda _, textbox_value: update_textbox(textbox_value, "4"), inputs=[textbox], outputs=[textbox])
    button_5.click(lambda _, textbox_value: update_textbox(textbox_value, "5"), inputs=[textbox], outputs=[textbox])
    button_6.click(lambda _, textbox_value: update_textbox(textbox_value, "6"), inputs=[textbox], outputs=[textbox])
    button_mul.click(lambda _, textbox_value: update_textbox(textbox_value, "*"), inputs=[textbox], outputs=[textbox])

    button_1.click(lambda _, textbox_value: update_textbox(textbox_value, "1"), inputs=[textbox], outputs=[textbox])
    button_2.click(lambda _, textbox_value: update_textbox(textbox_value, "2"), inputs=[textbox], outputs=[textbox])
    button_3.click(lambda _, textbox_value: update_textbox(textbox_value, "3"), inputs=[textbox], outputs=[textbox])
    button_sub.click(lambda _, textbox_value: update_textbox(textbox_value, "-"), inputs=[textbox], outputs=[textbox])

    button_0.click(lambda _, textbox_value: update_textbox(textbox_value, "0"), inputs=[textbox], outputs=[textbox])
    button_dot.click(lambda _, textbox_value: update_textbox(textbox_value, "."), inputs=[textbox], outputs=[textbox])
    button_eq.click(lambda _, textbox_value: update_textbox(textbox_value, "="), inputs=[textbox], outputs=[textbox])
    button_add.click(lambda _, textbox_value: update_textbox(textbox_value, "+"), inputs=[textbox], outputs=[textbox])

    button_c.click(lambda _, __: clear_textbox(), inputs=None, outputs=[textbox])

    gr.Columns([gr.Rows([button_7, button_8, button_9, button_div]), 
                 gr.Rows([button_4, button_5, button_6, button_mul]), 
                 gr.Rows([button_1, button_2, button_3, button_sub]), 
                 gr.Rows([button_0, button_dot, button_eq, button_add])], 
                gr.Rows([button_c]))

if __name__ == "__main__":
    demo.launch()