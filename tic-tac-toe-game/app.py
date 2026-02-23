import gradio as gr
import random

def update_board(board, move, player):
    if board[move] != "":
        return board, "Invalid move, try again."
    board[move] = player
    return board, ""

def check_winner(board):
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Tie"
    return False

def system_move(board):
    available_moves = [i for i, x in enumerate(board) if x == ""]
    if not available_moves:
        return board
    move = random.choice(available_moves)
    board[move] = "O"
    return board

def play_game(move, board, player):
    board, message = update_board(board, move-1, player)
    winner = check_winner(board)
    if winner:
        return board, f"Game over, {winner} wins!" if winner != "Tie" else "Game over, it's a tie!"
    board = system_move(board)
    winner = check_winner(board)
    if winner:
        return board, f"Game over, {winner} wins!" if winner != "Tie" else "Game over, it's a tie!"
    return board, message

def reset_game():
    return ([""] * 9, "")

demo = gr.Blocks()

with demo:
    gr.Markdown("# Tic Tac Toe Game")
    board = [""] * 9
    player = "X"
    move = gr.Number(label="Move (1-9)", value=1)
    board_output = gr.JSON(label="Board")
    message_output = gr.Textbox(label="Message")
    play_button = gr.Button("Play")
    reset_button = gr.Button("Reset")

    play_button.click(
        play_game,
        inputs=[move, board_output, player],
        outputs=[board_output, message_output],
    )

    reset_button.click(
        reset_game,
        outputs=[board_output, message_output],
    )

    board_output.change(
        lambda x: "\n".join([f"{x[i*3]} | {x[i*3+1]} | {x[i*3+2]}" for i in range(3)]),
        inputs=board_output,
        outputs=board_output,
    )

if __name__ == "__main__":
    demo.launch()