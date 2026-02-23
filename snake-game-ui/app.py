import gradio as gr
import random

# Initialize game state
snake_body = [(0, 0)]
food_position = (5, 5)
score = 0
direction = 'Right'
paused = False

# Function to update game state
def update_game(state):
    global snake_body, food_position, score, direction, paused
    if not paused:
        head = snake_body[-1]
        if direction == 'Up':
            new_head = (head[0], head[1] - 1)
        elif direction == 'Down':
            new_head = (head[0], head[1] + 1)
        elif direction == 'Left':
            new_head = (head[0] - 1, head[1])
        elif direction == 'Right':
            new_head = (head[0] + 1, head[1])
        
        snake_body.append(new_head)
        
        if snake_body[-1] == food_position:
            score += 1
            food_position = (random.randint(0, 9), random.randint(0, 9))
        else:
            snake_body.pop(0)
        
        # Check for collision with wall or self
        if (snake_body[-1][0] < 0 or snake_body[-1][0] > 9 or 
            snake_body[-1][1] < 0 or snake_body[-1][1] > 9 or 
            snake_body[-1] in snake_body[:-1]):
            paused = True
    
    # Create game board
    board = ''
    for y in range(10):
        for x in range(10):
            if (x, y) in snake_body:
                board += '<span style="background-color: green; width: 20px; height: 20px; display: inline-block;"></span>'
            elif (x, y) == food_position:
                board += '<span style="background-color: red; width: 20px; height: 20px; display: inline-block;"></span>'
            else:
                board += '<span style="background-color: gray; width: 20px; height: 20px; display: inline-block;"></span>'
        board += '<br>'
    
    return board, score, paused

# Function to handle button clicks
def handle_button_click(button, state):
    global direction, paused
    if button == 'Start':
        paused = False
    elif button == 'Pause':
        paused = True
    elif button == 'Reset':
        global snake_body, food_position, score, direction
        snake_body = [(0, 0)]
        food_position = (5, 5)
        score = 0
        direction = 'Right'
        paused = False
    elif button == 'Up':
        direction = 'Up'
    elif button == 'Down':
        direction = 'Down'
    elif button == 'Left':
        direction = 'Left'
    elif button == 'Right':
        direction = 'Right'
    
    return update_game(state)

# Create Gradio UI
demo = gr.Blocks()

# Score display
with demo:
    gr.HTML('<h1>Score: <span id="score">0</span></h1>')

    # Game board
    gr.HTML('<div id="game-board"></div>')

    # Button controls
    with gr.Row():
        gr.Button('Start').click(
            handle_button_click, 
            inputs=['Start'], 
            outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')]
        )
        gr.Button('Pause').click(
            handle_button_click, 
            inputs=['Pause'], 
            outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')]
        )
        gr.Button('Reset').click(
            handle_button_click, 
            inputs=['Reset'], 
            outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')]
        )

    # Arrow key controls
    with gr.Row():
        gr.Button('Up').click(
            handle_button_click, 
            inputs=['Up'], 
            outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')]
        )
        gr.Button('Down').click(
            handle_button_click, 
            inputs=['Down'], 
            outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')]
        )
        gr.Button('Left').click(
            handle_button_click, 
            inputs=['Left'], 
            outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')]
        )
        gr.Button('Right').click(
            handle_button_click, 
            inputs=['Right'], 
            outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')]
        )

# Update game state every second
def update_state(state):
    return update_game(state)

demo.queue(update_state, inputs=[gr.State()], outputs=[gr.HTML('game-board'), gr.Number(label='Score'), gr.Boolean(label='Paused')], every=1000)

if __name__ == "__main__":
    demo.launch()