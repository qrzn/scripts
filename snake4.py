import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Set up the Snake class
class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.change_direction_to = self.direction
    
    def change_direction(self, new_direction):
        if new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
    
    def update(self):
        if self.direction == "RIGHT":
            self.position[0] += 10
        elif self.direction == "LEFT":
            self.position[0] -= 10
        elif self.direction == "UP":
            self.position[1] -= 10
        elif self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0, list(self.position))
        if self.position[0] == food.position[0] and self.position[1] == food.position[1]:
            food.generate_food()
        else:
            self.body.pop()
    
    def check_collision(self):
        if self.position[0] > window_width - 10 or self.position[0] < 0:
            return True
        elif self.position[1] > window_height - 10 or self.position[1] < 0:
            return True
        for body_part in self.body[1:]:
            if self.position[0] == body_part[0] and self.position[1] == body_part[1]:
                return True
        return False
    
    def draw(self, surface):
        for body_part in self.body:
            pygame.draw.rect(surface, black, pygame.Rect(body_part[0], body_part[1], 10, 10))

# Set up the Food class
class Food:
    def __init__(self):
        self.position = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
    
    def generate_food(self):
        self.position = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
    
    def draw(self, surface):
        pygame.draw.rect(surface, red, pygame.Rect(self.position[0], self.position[1], 10, 10))

# Create instances of Snake and Food
snake = Snake()
food = Food()

# Set up the game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
    
    snake.update()
    
    if snake.check_collision():
        game_over = True
    
    window.fill(white)
    snake.draw(window)
    food.draw(window)
    pygame.display.update()
    
    clock.tick(20)

# Quit the game
pygame.quit()
