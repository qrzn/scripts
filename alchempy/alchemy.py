import json

# Define the game elements
elements = {
    'fire': {
        'properties': ['hot', 'bright'],
        'combinations': ['fire + water = steam', 'fire + earth = lava']
    },
    'water': {
        'properties': ['wet', 'cool'],
        'combinations': ['water + earth = mud', 'water + fire = steam']
    },
    'earth': {
        'properties': ['solid', 'grounded'],
        'combinations': ['earth + water = mud', 'earth + fire = lava']
    },
    'air': {
        'properties': ['light', 'gaseous'],
        'combinations': ['air + fire = smoke', 'air + water = mist']
    },
}

# Save the game state to a file
def save_game_state(game_state, file_path):
    with open(file_path, 'w') as file:
        json.dump(game_state, file)

# Load the game state from a file
def load_game_state(file_path):
    with open(file_path, 'r') as file:
        game_state = json.load(file)
    return game_state

# Game loop
while True:
    # Display available elements
    print("Available Elements:")
    for element in elements:
        print(element)

    # Get user input for element selection
    user_input = input("Select an element or 'q' to quit: ")

    # Check if the user wants to quit
    if user_input.lower() == 'q':
        print("Exiting the game...")
        break

    # Validate and process the selected element
    if user_input in elements:
        selected_element = user_input
        print(f"You selected {selected_element}!")
        # Perform actions based on the selected element
        # ...
    else:
        print("Invalid element. Try again.")

# Rest of the code...

