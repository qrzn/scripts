def display_menu():
    games = [
        {"name": "Game 1", "category": "Action"},
        {"name": "Game 2", "category": "Adventure"},
        {"name": "Game 3", "category": "Puzzle"},
        # Add more games here
    ]
    
    categories = set(game["category"] for game in games)
    categories = sorted(categories)
    
    print("Welcome to the Game Launcher!")
    print("Please select a category:")
    
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")
    
    print("0. Exit")
    
    category_choice = input("Enter your choice (0-{0}): ".format(len(categories)))
    
    if category_choice == "0":
        return
    
    selected_category = categories[int(category_choice) - 1]
    
    clear_screen()
    
    print(f"Available games in the '{selected_category}' category:")
    
    for game in games:
        if game["category"] == selected_category:
            print(game["name"])
    
    game_choice = input("Enter the number of the game you want to play: ")
    
    if game_choice == "0":
        return
    
    selected_game = games[int(game_choice) - 1]["name"]
    
    clear_screen()
    
    print(f"Launching '{selected_game}'...")
    # Add code to launch the selected game here

