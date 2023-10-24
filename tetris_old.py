import sys
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRID_SIZE = 30

# Tetris shapes
SHAPES = [
    [[1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
]

# Initialize variables
grid = [[0 for _ in range(SCREEN_WIDTH // GRID_SIZE)] for _ in range(SCREEN_HEIGHT // GRID_SIZE)]
current_shape = random.choice(SHAPES)
current_pos = [0, 0]

def draw_grid():
    for i in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(SCREEN, WHITE, (i, 0), (i, SCREEN_HEIGHT))
    for i in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(SCREEN, WHITE, (0, i), (SCREEN_WIDTH, i))

def draw_shape(shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(SCREEN, BLUE, (offset[0] + x * GRID_SIZE, offset[1] + y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def valid_move(shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            try:
                # Check if it's outside the grid or colliding
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
    global current_shape, current_pos, grid
    for y, row in enumerate(current_shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + current_pos[1] // GRID_SIZE][x + current_pos[0] // GRID_SIZE] = 1
    current_shape = random.choice(SHAPES)
    current_pos = [0, 0]

def remove_line():
    global grid
    for i, row in enumerate(grid[:-1]):
        if all(cell for cell in row):
            del grid[i]
            grid.insert(0, [0 for _ in range(SCREEN_WIDTH // GRID_SIZE)])

def draw_merged_shapes():
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(SCREEN, BLUE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# ... (the rest of your code stays the same up until the main loop)

# New variables to control the timing
fall_time = 0
fall_speed = 500  # milliseconds
last_fall_time = pygame.time.get_ticks()

while True:
    SCREEN.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Left movement
    if keys[pygame.K_LEFT]:
        new_pos = [current_pos[0] - GRID_SIZE, current_pos[1]]
        if valid_move(current_shape, new_pos):
            current_pos = new_pos
    # Right movement
    if keys[pygame.K_RIGHT]:
        new_pos = [current_pos[0] + GRID_SIZE, current_pos[1]]
        if valid_move(current_shape, new_pos):
            current_pos = new_pos
    # Down movement
    if keys[pygame.K_DOWN]:
        new_pos = [current_pos[0], current_pos[1] + GRID_SIZE]
        if valid_move(current_shape, new_pos):
            current_pos = new_pos
    # Rotation
    if keys[pygame.K_SPACE]:
        new_shape = [list(row) for row in zip(*reversed(current_shape))]
        if valid_move(new_shape, current_pos):
            current_shape = new_shape

    # Automatic falling
    if current_time - last_fall_time > fall_speed:
        if valid_move(current_shape, [current_pos[0], current_pos[1] + GRID_SIZE]):
            current_pos[1] += GRID_SIZE
        else:
            merge_shape()
            remove_line()
        last_fall_time = current_time

    draw_grid()
    draw_shape(current_shape, current_pos)
    draw_merged_shapes()
    pygame.display.update()
    CLOCK.tick(30)  # Changed to 30 FPS for more responsive controls
