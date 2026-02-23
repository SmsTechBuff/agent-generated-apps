import gradio as gr
import random

# Initialize game state
snake_body = [(0, 0)]
food = (5, 5)
score = 0
direction = 'right'
paused = False

# Define game board size
board_size = 10

# Function to update game state
def update_game_state(direction, snake_body, food, score, paused):
    if not paused:
        head = snake_body[-1]
        if direction == 'up':
            new_head = (head[0], head[1] - 1)
        elif direction == 'down':
            new_head = (head[0], head[1] + 1)
        elif direction == 'left':
            new_head = (head[0] - 1, head[1])
        elif direction == 'right':
            new_head = (head[0] + 1, head[1])
        
        # Check collision with food
        if new_head == food:
            score += 1
            food = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        else:
            snake_body.pop(0)
        
        # Check collision with wall or self
        if (new_head[0] < 0 or new_head[0] >= board_size or 
            new_head[1] < 0 or new_head[1] >= board_size or 
            new_head in snake_body):
            return 'Game Over', snake_body, food, score, True
        
        snake_body.append(new_head)
    
    return direction, snake_body, food, score, paused

# Function to draw game board
def draw_game_board(snake_body, food):
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    for x, y in snake_body:
        board[y][x] = 'S'
    board[food[1]][food[0]] = 'F'
    return '\n'.join([' '.join(row) for row in board])

# Create Gradio app
demo = gr.Blocks()

# Create game board HTML component
game_board = gr.HTML(value=draw_game_board(snake_body, food))

# Create score display HTML component
score_display = gr.HTML(value=f'Score: {score}')

# Create buttons
start_button = gr.Button('Start')
pause_button = gr.Button('Pause')
reset_button = gr.Button('Reset')
up_button = gr.Button('Up')
down_button = gr.Button('Down')
left_button = gr.Button('Left')
right_button = gr.Button('Right')

# Create state variables
direction_state = gr.State(value=direction)
snake_body_state = gr.State(value=snake_body)
food_state = gr.State(value=food)
score_state = gr.State(value=score)
paused_state = gr.State(value=paused)

# Define event handlers
def start_game(event):
    return 'right', snake_body, food, score, False

def pause_game(event):
    return direction, snake_body, food, score, not paused

def reset_game(event):
    return 'right', [(0, 0)], (5, 5), 0, False

def move_up(event):
    return 'up', snake_body, food, score, paused

def move_down(event):
    return 'down', snake_body, food, score, paused

def move_left(event):
    return 'left', snake_body, food, score, paused

def move_right(event):
    return 'right', snake_body, food, score, paused

def update_state(direction, snake_body, food, score, paused):
    new_direction, new_snake_body, new_food, new_score, new_paused = update_game_state(direction, snake_body, food, score, paused)
    return draw_game_board(new_snake_body, new_food), new_score, new_direction, new_snake_body, new_food, new_score, new_paused

# Link event handlers to buttons
start_button.click(start_game, inputs=None, outputs=[direction_state, snake_body_state, food_state, score_state, paused_state])
pause_button.click(pause_game, inputs=None, outputs=[direction_state, snake_body_state, food_state, score_state, paused_state])
reset_button.click(reset_game, inputs=None, outputs=[direction_state, snake_body_state, food_state, score_state, paused_state])
up_button.click(move_up, inputs=None, outputs=[direction_state, snake_body_state, food_state, score_state, paused_state])
down_button.click(move_down, inputs=None, outputs=[direction_state, snake_body_state, food_state, score_state, paused_state])
left_button.click(move_left, inputs=None, outputs=[direction_state, snake_body_state, food_state, score_state, paused_state])
right_button.click(move_right, inputs=None, outputs=[direction_state, snake_body_state, food_state, score_state, paused_state])

# Link state variables to update function
direction_state.change(update_state, inputs=[direction_state, snake_body_state, food_state, score_state, paused_state], outputs=[game_board, score_state, direction_state, snake_body_state, food_state, score_state, paused_state])

# Create app layout
with demo:
    gr.Row(score_display)
    gr.Row(game_board)
    with gr.Row():
        start_button
        pause_button
        reset_button
    with gr.Row():
        up_button
        down_button
        left_button
        right_button

if __name__ == "__main__":
    demo.launch()