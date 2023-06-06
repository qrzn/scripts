# Create instances of Snake, Food, Menu, and Prompt
snake = Snake()
food = Food()
menu = Menu()
prompt = Prompt()

# Set up the game loop
clock = pygame.time.Clock()
game_over = False
game_running = False
show_prompt = False
score = 0

# Set up the score font
score_font = pygame.font.Font(None, 36)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if game_running:
                # ... game input handling code as before ...
            else:
                menu_result = menu.handle_input(event)
                if menu_result == "start":
                    game_running = True
                elif menu_result == "quit":
                    game_over = True
    
    if game_running:
        # ... game update code as before ...
    
    window.fill(white)
    
    if game_running:
        # ... game drawing code as before ...
        
        # Draw the score on the screen
        score_text = score_font.render("Score: " + str(score), True, black)
        window.blit(score_text, (10, 10))
    else:
        menu.draw(window)
    
    pygame.display.update()
    
    clock.tick(20)

    if game_running and snake.check_collision():
        game_running = False
        show_prompt = True

    if game_running and snake.head.position == food.position:
        snake.eat_food()
        score += 1
        food.generate_position()

    if show_prompt:
        prompt_result = prompt_restart()
        if prompt_result == "yes":
            snake = Snake()
            food = Food()
            game_running = True
            show_prompt = False
            score = 0
        elif prompt_result == "no":
            game_running = False  # Go back to the menu
            show_prompt = False
        elif prompt_result == "menu":
            game_running = False
            show_prompt = False

# Quit the game
pygame.quit()
