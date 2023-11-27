import sys
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the title of the window
pygame.display.set_caption('Pytris 1.0')

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRID_SIZE = 30

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Define shapes with their unique colors
SHAPES = [
    {'shape': [[1], [1], [1], [1]], 'color': RED},
    {'shape': [[1, 1], [1, 1]], 'color': GREEN},
    {'shape': [[0, 1, 0], [1, 1, 1]], 'color': BLUE},
    {'shape': [[1, 0, 0], [1, 1, 1]], 'color': YELLOW},
    {'shape': [[0, 0, 1], [1, 1, 1]], 'color': ORANGE},
    {'shape': [[1, 1, 0], [0, 1, 1]], 'color': PURPLE},
    {'shape': [[0, 1, 1], [1, 1, 0]], 'color': CYAN},
]

# Initialize variables
grid = [[0 for _ in range(SCREEN_WIDTH // GRID_SIZE)] for _ in range(SCREEN_HEIGHT // GRID_SIZE)]
current_shape = random.choice(SHAPES)
current_pos = [0, 0]
fall_time = 0
fall_speed = 250  # milliseconds
last_fall_time = pygame.time.get_ticks()
space_down = False  # For controlling rotation
last_move_time = 0
move_delay = 300  # in milliseconds
cleared_lines = 0
# Select a random shape and its color
selected_shape = random.choice(SHAPES)
current_shape = selected_shape['shape']
current_color = selected_shape['color']

    # Initialize font for displaying cleared lines
font = pygame.font.Font(None, 36)

def remove_line():
    global cleared_lines  # Declare as global to modify it
    for i, row in enumerate(grid[:-1]):
        if all(cell for cell in row):
            del grid[i]
            grid.insert(0, [0 for _ in range(SCREEN_WIDTH // GRID_SIZE)])
            cleared_lines += 1  # Increment the counter

def draw_grid():
    for i in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(SCREEN, WHITE, (i, 0), (i, SCREEN_HEIGHT))
    for i in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(SCREEN, WHITE, (0, i), (SCREEN_WIDTH, i))

def draw_shape(shape, position):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(SCREEN, current_color, (position[0] + x * GRID_SIZE, position[1] + y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def valid_move(shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            try:
                if cell:
                    if x + offset[0] // GRID_SIZE < 0 or \
                       x + offset[0] // GRID_SIZE >= (SCREEN_WIDTH // GRID_SIZE) or \
                       y + offset[1] // GRID_SIZE >= (SCREEN_HEIGHT // GRID_SIZE) or \
                       grid[y + offset[1] // GRID_SIZE][x + offset[0] // GRID_SIZE]:
                        return False
            except IndexError:
                return False
    return True

def merge_shape():
    global grid  # assuming your grid is a global variable
    for y, row in enumerate(current_shape):
        for x, cell in enumerate(row):
            if cell:
                grid[(current_pos[1] + y * GRID_SIZE) // GRID_SIZE][(current_pos[0] + x * GRID_SIZE) // GRID_SIZE] = current_color

def draw_merged_shapes():
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            if color:
                pygame.draw.rect(SCREEN, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def display_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over', True, WHITE)
    SCREEN.blit(text, [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3])
    pygame.display.flip()

def game_over():
    for cell in grid[0]:
        if cell:
            display_game_over()
            
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        waiting = False
                        
            return True
    return False

while True:
    # Check for Game Over
    if game_over():
        print("Game Over!")
        pygame.quit()
        sys.exit()

    SCREEN.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not space_down:
                new_shape = [list(row) for row in zip(*reversed(current_shape))]
                if valid_move(new_shape, current_pos):
                    current_shape = new_shape
                space_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_down = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        new_pos = [current_pos[0] - GRID_SIZE, current_pos[1]]
        if valid_move(current_shape, new_pos):
            current_pos = new_pos
    if keys[pygame.K_RIGHT]:
        new_pos = [current_pos[0] + GRID_SIZE, current_pos[1]]
        if valid_move(current_shape, new_pos):
            current_pos = new_pos
    if keys[pygame.K_DOWN]:
        new_pos = [current_pos[0], current_pos[1] + GRID_SIZE]
        if valid_move(current_shape, new_pos):
            current_pos = new_pos

    last_move_time = current_time

    if current_time - last_fall_time > fall_speed:
    	if valid_move(current_shape, [current_pos[0], current_pos[1] + GRID_SIZE]):
        	current_pos[1] += GRID_SIZE
    	else:
        	merge_shape()
        	remove_line()
        # Select a new random shape and its color
        	selected_shape = random.choice(SHAPES)
        	current_shape = selected_shape['shape']
        	current_color = selected_shape['color']
        	# Reset the position to the top of the screen
        	current_pos = [0, 0]
    	last_fall_time = current_time


    draw_grid()
    draw_shape(current_shape, current_pos)
    draw_merged_shapes()

    # Display cleared lines count
    text_surface = font.render(f'Cleared Lines: {cleared_lines}', True, (255, 255, 255))
    SCREEN.blit(text_surface, (10, 10))

    pygame.display.update()
    CLOCK.tick(10)

