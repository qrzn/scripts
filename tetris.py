import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[1, 1, 1], [0, 0, 1]],  # J shape
    [[1, 1, 1], [1, 0, 0]]  # L shape
]

# Initialize game variables
grid = [[BLACK] * 10 for _ in range(20)]
current_shape = random.choice(SHAPES)
shape_color = random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
shape_x = 3
shape_y = 0
score = 0

# Game loop
clock = pygame.time.Clock()
run = True
fall_time = 0
fall_speed = 0.5  # Time delay (in seconds) between shape movements

def draw_grid():
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(win, color, (x * 30, y * 30, 30, 30))

def draw_shape():
    for y, row in enumerate(current_shape):
        for x, value in enumerate(row):
            if value:
                pygame.draw.rect(win, shape_color, ((shape_x + x) * 30, (shape_y + y) * 30, 30, 30))

def check_collision():
    for y, row in enumerate(current_shape):
        for x, value in enumerate(row):
            if value and (grid[shape_y + y][shape_x + x] != BLACK or shape_y + y >= 20 or shape_x + x < 0 or shape_x + x >= 10):
                return True
    return False

def merge_shape():
    for y, row in enumerate(current_shape):
        for x, value in enumerate(row):
            if value:
                grid[shape_y + y][shape_x + x] = shape_color

def clear_rows():
    global score
    full_rows = [row for row in grid if all(cell != BLACK for cell in row)]
    for row in full_rows:
        grid.remove(row)
        grid.insert(0, [BLACK] * 10)
        score += 1

def game_over():
    font = pygame.font.Font(None, 80)
    text = font.render("Game Over", True, RED)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Game loop
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shape_x -= 1
                if check_collision():
                    shape_x += 1
            elif event.key == pygame.K_RIGHT:
                shape_x += 1
                if check_collision():
                    shape_x -= 1
            elif event.key == pygame.K_DOWN:
                shape_y += 1
                if check_collision():
                    shape_y -= 1
            elif event.key == pygame.K_SPACE:
                rotated_shape = [[current_shape[j][i] for j in range(len(current_shape))] for i in range(len(current_shape[0]))]
                if not check_collision():
                    current_shape = rotated_shape

    # Shape falling
    if pygame.time.get_ticks() - fall_time > fall_speed * 1000:
        shape_y += 1
        if check_collision():
            shape_y -= 1
            merge_shape()
            clear_rows()
            if any(cell != BLACK for cell in grid[0]):
                run = False
            current_shape = random.choice(SHAPES)
            shape_color = random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
            shape_x = 3
            shape_y = 0
        fall_time = pygame.time.get_ticks()

    # Draw the game window
    win.fill(WHITE)
    draw_grid()
    draw_shape()
    pygame.display.flip()
    clock.tick(60)

# Game over
game_over()
pygame.quit()

