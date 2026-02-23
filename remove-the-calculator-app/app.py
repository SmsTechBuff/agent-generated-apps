import gradio as gr

# Calculator app (commented out as per requirement)
# def calculate(num1, num2, operation):
#     if operation == "Addition":
#         return num1 + num2
#     elif operation == "Subtraction":
#         return num1 - num2
#     elif operation == "Multiplication":
#         return num1 * num2
#     elif operation == "Division":
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Invalid operation"

# demo = gr.Interface(
#     fn=calculate,
#     inputs=[
#         gr.Number(label="Number 1"),
#         gr.Number(label="Number 2"),
#         gr.Radio(
#             choices=["Addition", "Subtraction", "Multiplication", "Division"],
#             label="Operation",
#         ),
#     ],
#     outputs="number",
#     title="Calculator App",
#     description="A simple calculator app.",
# )

# Since the calculator app is removed, we will create a new simple app
def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Please enter your name."

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Hello World App",
    description="A simple app that greets you by name.",
)

if __name__ == "__main__":
    demo.launch()