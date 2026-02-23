import gradio as gr
import random

def update_board(move, board):
    """
    Updates the Tic Tac Toe board based on the player's move.

    Args:
        move (int): The player's move (0-8).
        board (list): The current state of the board.

    Returns:
        tuple: The updated board and the result of the move.
    """
    if board[move] != "":
        return board, "Invalid move, try again."
    board[move] = "X"
    if check_win(board, "X"):
        return board, "You win!"
    elif check_draw(board):
        return board, "It's a draw!"
    else:
        computer_move = get_computer_move(board)
        board[computer_move] = "O"
        if check_win(board, "O"):
            return board, "Computer wins!"
        elif check_draw(board):
            return board, "It's a draw!"
        else:
            return board, ""

def check_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board (list): The current state of the board.
        player (str): The player to check for (X or O).

    Returns:
        bool: True if the player has won, False otherwise.
    """
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw.

    Args:
        board (list): The current state of the board.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return "" not in board

def get_computer_move(board):
    """
    Gets the computer's move.

    Args:
        board (list): The current state of the board.

    Returns:
        int: The computer's move (0-8).
    """
    possible_moves = [i for i, x in enumerate(board) if x == ""]
    return random.choice(possible_moves)

demo = gr.Blocks()

with demo:
    gr.Markdown("# Tic Tac Toe Game")
    board = [""] * 9
    move_input = gr.Number(label="Enter your move (1-9)")
    output = gr.Textbox(label="Result")
    board_output = gr.Textbox(label="Board")

    def update(move):
        nonlocal board
        if move < 1 or move > 9:
            return "\n".join([" | ".join(board[i:i+3]) for i in range(0, 9, 3)]), "Invalid move, try again.", board
        new_board, result = update_board(move - 1, board[:]) # Create a copy of the board
        board_str = "\n".join([" | ".join(new_board[i:i+3]) for i in range(0, 9, 3)])
        board[:] = new_board # Update the board
        return board_str, result, board

    button = gr.Button("Make Move")
    button.click(update, inputs=move_input, outputs=[board_output, output, board_output])

if __name__ == "__main__":
    demo.launch()