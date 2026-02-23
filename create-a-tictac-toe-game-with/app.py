import gradio as gr
import random

# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to check if the game is won
def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Function to handle the game logic
def play_game(clicks):
    global board
    if clicks is None:
        return board, "Your turn"
    row, col = clicks
    if board[row][col] != ' ':
        return board, "Invalid move, try again"
    board[row][col] = 'X'
    winner = check_win(board)
    if winner is not None:
        return board, f"Game over, {winner} wins"
    # System's turn
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        system_row, system_col = random.choice(empty_cells)
        board[system_row][system_col] = 'O'
        winner = check_win(board)
        if winner is not None:
            return board, f"Game over, {winner} wins"
    return board, "Your turn"

# Create the Gradio interface
demo = gr.Interface(
    play_game,
    gr.Grid(
        [gr.Button(label=" ") for _ in range(9)],
        rows=3,
        columns=3,
        show_label=False
    ),
    [gr.Grid(
        [gr.Textbox(label=" ") for _ in range(9)],
        rows=3,
        columns=3,
        show_label=False
    ), gr.Textbox(label="Message")],
    title="Tic Tac Toe Game",
    description="Play Tic Tac Toe against the system"
)

if __name__ == "__main__":
    demo.launch()