import gradio as gr

def update_board(board, move, turn):
    if board[move] != "":
        return board, "Invalid move, try again.", turn
    board[move] = turn
    return board, "", turn

def check_winner(board):
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Tie"
    return False

def switch_turn(turn):
    if turn == "X":
        return "O"
    else:
        return "X"

def check_winner_and_update_result(board, result, turn):
    winner = check_winner(board)
    if winner:
        if winner == "Tie":
            return "It's a tie!", turn
        else:
            return f"Player {winner} wins!", turn
    else:
        return result, turn

def reset_board(board):
    return [""] * 9, "", "X"

demo = gr.Blocks()

with demo:
    gr.Markdown("# Tic Tac Toe")
    board = gr.State(value=[""] * 9)
    turn = gr.State(value="X")
    result = gr.State(value="")
    
    with gr.Columns():
        with gr.Column():
            gr.Button("Reset").click(
                reset_board,
                inputs=None,
                outputs=[board, result, turn],
                queue=False
            )
        with gr.Column():
            gr.Textbox(label="Result", source=result)
    
    with gr.Columns():
        with gr.Column():
            gr.Button("1").click(
                update_board,
                inputs=[board, 0, turn],
                outputs=[board, result, turn],
                queue=False
            )
        with gr.Column():
            gr.Button("2").click(
                update_board,
                inputs=[board, 1, turn],
                outputs=[board, result, turn],
                queue=False
            )
        with gr.Column():
            gr.Button("3").click(
                update_board,
                inputs=[board, 2, turn],
                outputs=[board, result, turn],
                queue=False
            )
    
    with gr.Columns():
        with gr.Column():
            gr.Button("4").click(
                update_board,
                inputs=[board, 3, turn],
                outputs=[board, result, turn],
                queue=False
            )
        with gr.Column():
            gr.Button("5").click(
                update_board,
                inputs=[board, 4, turn],
                outputs=[board, result, turn],
                queue=False
            )
        with gr.Column():
            gr.Button("6").click(
                update_board,
                inputs=[board, 5, turn],
                outputs=[board, result, turn],
                queue=False
            )
    
    with gr.Columns():
        with gr.Column():
            gr.Button("7").click(
                update_board,
                inputs=[board, 6, turn],
                outputs=[board, result, turn],
                queue=False
            )
        with gr.Column():
            gr.Button("8").click(
                update_board,
                inputs=[board, 7, turn],
                outputs=[board, result, turn],
                queue=False
            )
        with gr.Column():
            gr.Button("9").click(
                update_board,
                inputs=[board, 8, turn],
                outputs=[board, result, turn],
                queue=False
            )
    
    with gr.Columns():
        with gr.Column():
            gr.Textbox(label="Board", source=board)

    board, result, turn = update_board(board.value, 0, turn.value)
    result, turn = check_winner_and_update_result(board, result, turn)
    turn = switch_turn(turn)

if __name__ == "__main__":
    demo.launch()