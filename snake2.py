import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Nehebkau")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
magenta = pygame.Color(255, 0, 255)

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

# Set up the Menu class
class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("Nehebkau", True, magenta)
        self.start_game_text = self.font.render("Start Game", True, white)
        self.quit_text = self.font.render("Quit", True, white)
        self.selected_option = 0

    def draw(self, surface):
        surface.fill(black)
        surface.blit(self.title_text, (350, 100))
        if self.selected_option == 0:
            pygame.draw.rect(surface, green, pygame.Rect(300, 200, 200, 50))
        else:
            pygame.draw.rect(surface, white, pygame.Rect(300, 200, 200, 50))
        if self.selected_option == 1:
            pygame.draw.rect(surface, green, pygame.Rect(300, 300, 200, 50))
        else:
            pygame.draw.rect(surface, white, pygame.Rect(300, 300, 200, 50))
        surface.blit(self.start_game_text, (350, 210))
        surface.blit(self.quit_text, (375, 310))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % 2
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % 2
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    return "start"
                elif self.selected_option == 1:
                    return "quit"

# Set up the Prompt class
class Prompt:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Play again? (Y/N)", True, white)

    def draw(self, surface):
        surface.fill(black)
        surface.blit(self.text, (300, 250))

# Create instances of Snake, Food, and Menu
snake = Snake()
food = Food()
menu = Menu()
prompt = Prompt()

# Set up the game loop
clock = pygame.time.Clock()
game_over = False
game_running = False
paused = False

def prompt_restart():
    window.fill(black)
    prompt.draw(window)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if game_running and not paused:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_p:
                    paused = True
            elif game_running and paused:
                if event.key == pygame.K_p:
                    paused = False
            else:
                menu_result = menu.handle_input(event)
                if menu_result == "start":
                    game_running = True
                elif menu_result == "quit":
                    game_over = True
    
    if game_running and not paused:
        snake.update()
        if snake.check_collision():
            game_running = False
            prompt_result = prompt_restart()
            if prompt_result:
                snake = Snake()
                food = Food()
                game_running = True
            else:
                game_over = True
    
    window.fill(white)
    
    if game_running:
        snake.draw(window)
        food.draw(window)
        if paused:
            pause_text = menu.font.render("Paused", True, black)
            window.blit(pause_text, (380, 10))
    else:
        menu.draw(window)
    
    pygame.display.update()
    
    clock.tick(20)

# Quit the game
pygame.quit()
