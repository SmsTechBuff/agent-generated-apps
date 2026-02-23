import gradio as gr
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def is_valid_move(self, move):
        return self.board[move] == ' '

    def make_move(self, move):
        if self.is_valid_move(move):
            self.board[move] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return False

    def get_board(self):
        return [self.board[i:i+3] for i in range(0, 9, 3)]

def update_board(move):
    game.make_move(move)
    board = game.get_board()
    winner = game.check_winner()
    if winner:
        if winner == 'Tie':
            return board, "It's a tie!", False
        else:
            return board, f"Player {winner} wins!", False
    return board, "", True

def reset_game():
    game.reset()
    return game.get_board(), "", True

game = TicTacToe()

demo = gr.Blocks()

with demo:
    gr.Header("Tic Tac Toe")
    board = gr.Grid(label="Board", shape=(3, 3), cell_type="text")
    move = gr.Button("Make Move")
    reset = gr.Button("Reset")
    result = gr.Textbox(label="Result")
    playable = gr.Number(label="Playable", value=1)

    move.click(
        update_board,
        inputs=[gr.Number(label="Move", value=0)],
        outputs=[board, result, playable],
    )

    reset.click(
        reset_game,
        outputs=[board, result, playable],
    )

if __name__ == "__main__":
    demo.launch()