import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 50
CELL_SIZE = 50

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

def draw_board(board, screen, cell_size):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == 1:  # Draw wall
                pygame.draw.rect(screen, WHITE, rect)
            elif cell == 2:  # Draw pellet
                pellet_center = (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2)
                pygame.draw.circle(screen, WHITE, pellet_center, cell_size // 8)

# 0 = empty, 1 = wall, 2 = pellet
board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
    [1, 2, 2, 2, 1, 1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Clone")

# Initialize variables
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
clock = pygame.time.Clock()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Draw everything
    screen.fill(BLACK)
    draw_board(board, screen, CELL_SIZE)
    pygame.draw.circle(screen, YELLOW, player_pos, PLAYER_SIZE // 2)

    pygame.display.flip()
    clock.tick(30)
