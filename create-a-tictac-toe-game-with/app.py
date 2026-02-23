import gradio as gr
import random

def update_board(board, row, col, turn):
    if board[row][col] == "":
        board[row][col] = turn
        return board
    else:
        return board

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def system_turn(board):
    possible_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if possible_moves:
        i, j = random.choice(possible_moves)
        board[i][j] = "O"
    return board

def play_game(row, col, board, turn):
    board = update_board(board, row, col, turn)
    winner = check_winner(board)
    if winner:
        return board, f"Player {winner} wins!"
    elif all(all(cell != "" for cell in row) for row in board):
        return board, "It's a draw!"
    board = system_turn(board)
    winner = check_winner(board)
    if winner:
        return board, f"Player {winner} wins!"
    elif all(all(cell != "" for cell in row) for row in board):
        return board, "It's a draw!"
    return board, ""

demo = gr.Blocks()

with demo:
    gr.Markdown("# Tic Tac Toe Game")
    grid = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(gr.Button(label="", show_label=False))
        grid.append(row)

    state = gr.State(value=[["" for _ in range(3)] for _ in range(3)])
    result = gr.Textbox(label="Result")

    for i in range(3):
        for j in range(3):
            grid[i][j].click(
                lambda row=i, col=j: play_game(row, col, state.value, "X"),
                inputs=[state],
                outputs=[state, result, *[grid[x][y] for x in range(3) for y in range(3)]],
            )

    for i in range(3):
        for j in range(3):
            grid[i][j].style(rounded=True, height=100, width=100)

if __name__ == "__main__":
    demo.launch()