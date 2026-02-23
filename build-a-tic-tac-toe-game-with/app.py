import gradio as gr
import random

# Initialize the game board
board = [' ' for _ in range(9)]

# Function to check if a player has won
def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False

# Function to handle player move
def handle_move(move, board):
    if board[move] != ' ':
        return "Invalid move, try again."
    board[move] = 'X'
    result = check_win(board)
    if result:
        return result
    # Make a random move for the computer
    available_moves = [i for i, x in enumerate(board) if x == ' ']
    if available_moves:
        computer_move = random.choice(available_moves)
        board[computer_move] = 'O'
    result = check_win(board)
    if result:
        return result
    return board

# Create the Gradio interface
demo = gr.Interface(
    fn=handle_move,
    inputs=[gr.Number(label="Move (1-9)"), gr.State(board)],
    outputs=[gr.Textbox(label="Result"), gr.State(board)],
    title="Tic Tac Toe Game",
    description="Enter a number from 1 to 9 to make a move."
)

if __name__ == "__main__":
    demo.launch()