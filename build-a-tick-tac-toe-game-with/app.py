import gradio as gr
import random

def update_board(board, move, player):
    if board[move] != "":
        return board, "Invalid move, try again."
    board[move] = player
    return board, ""

def check_win(board):
    # Check rows
    for i in range(0, 81, 9):
        if board[i] == board[i+1] == board[i+2] == board[i+3] == board[i+4] == board[i+5] == board[i+6] == board[i+7] == board[i+8] != "":
            return board[i]
    # Check columns
    for i in range(9):
        if board[i] == board[i+9] == board[i+18] == board[i+27] == board[i+36] == board[i+45] == board[i+54] == board[i+63] == board[i+72] != "":
            return board[i]
    # Check diagonals
    if board[0] == board[10] == board[20] == board[30] == board[40] == board[50] == board[60] == board[70] == board[80] != "":
        return board[0]
    if board[8] == board[16] == board[24] == board[32] == board[40] == board[48] == board[56] == board[64] == board[72] != "":
        return board[8]
    return None

def play_game(move, board, player):
    board, message = update_board(board, move, player)
    if message:
        return board, message
    winner = check_win(board)
    if winner:
        return board, f"Player {winner} wins!"
    if "" not in board:
        return board, "It's a tie!"
    return board, ""

def reset_game():
    return [""] * 81, "X", ""

def create_game():
    return [""] * 81, "X", ""

demo = gr.Blocks()
with demo:
    gr.Markdown("# Tic Tac Toe Game")
    board = create_game()[0]
    player = create_game()[1]
    message = create_game()[2]
    board_state = gr.State(value=board)
    player_state = gr.State(value=player)
    message_state = gr.State(value=message)
    move_input = gr.Number(label="Move (1-81)", precision=0)
    move_button = gr.Button("Make Move")
    reset_button = gr.Button("Reset Game")
    board_output = gr.JSON(label="Board State")
    message_output = gr.Textbox(label="Game Message")
    move_button.click(
        play_game,
        inputs=[move_input, board_state, player_state],
        outputs=[board_state, message_output],
        queue=False
    )
    reset_button.click(
        reset_game,
        outputs=[board_state, player_state, message_output],
        queue=False
    )
    board_state.change(
        board_output,
        queue=False
    )

if __name__ == "__main__":
    demo.launch()