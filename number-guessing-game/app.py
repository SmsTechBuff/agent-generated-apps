import gradio as gr
import random

def guess_number(guess, number_to_guess, attempts):
    if guess == "":
        return "Please enter a number", number_to_guess, attempts
    try:
        guess = int(guess)
    except ValueError:
        return "Invalid input. Please enter a whole number.", number_to_guess, attempts
    attempts += 1
    if guess < number_to_guess:
        return f"Too low! You have {10 - attempts} attempts left.", number_to_guess, attempts
    elif guess > number_to_guess:
        return f"Too high! You have {10 - attempts} attempts left.", number_to_guess, attempts
    else:
        return f"Congratulations! You guessed the number in {attempts} attempts.", number_to_guess, attempts

demo = gr.Interface(
    fn=guess_number,
    inputs=[
        gr.Number(label="Guess a number between 1 and 100"),
        gr.State(value=random.randint(1, 100), label="Number to guess"),
        gr.State(value=0, label="Attempts")
    ],
    outputs="text",
    title="Number Guessing Game",
    description="Guess a number between 1 and 100. You have 10 attempts."
)

if __name__ == "__main__":
    demo.launch()