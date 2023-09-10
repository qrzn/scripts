import os
import json
import shutil
import subprocess
import time
import curses

# ANSI escape sequence constants (unchanged)
# ANSI escape sequence for text formatting
TEXT_BOLD = "\033[1m"
TEXT_RESET = "\033[0m"

# ANSI escape sequences for text colors
TEXT_COLOR_RED = "\033[31m"
TEXT_COLOR_GREEN = "\033[32m"
TEXT_COLOR_YELLOW = "\033[33m"
TEXT_COLOR_MAGENTA = "\033[35m"
TEXT_COLOR_RESET = "\033[0m"

# ANSI escape sequences for background colors
BACKGROUND_COLOR_BLUE = "\033[44m"
BACKGROUND_COLOR_WHITE = "\033[47m"
BACKGROUND_COLOR_RESET = "\033[49m"

# ANSI escape sequences for text colors
TEXT_COLOR_CYAN = "\033[36m"
TEXT_COLOR_RESET = "\033[0m"

# ANSI escape sequences for background colors
BACKGROUND_COLOR_BLACK = "\033[40m"
BACKGROUND_COLOR_RESET = "\033[49m"

# Load the JSON file
with open("game_data.json", "r") as file:
    data = json.load(file)

# Retrieve the game categories and commands
game_categories = data["categories"]
game_commands = data["commands"]

# Load the JSON file
with open("game_data.json", "r") as file:
    data = json.load(file)

# Retrieve the game categories and commands
game_categories = data["categories"]
game_commands = data["commands"]

def display_categories(stdscr, selected_category_idx):
    stdscr.clear()
    stdscr.addstr(0, 0, TEXT_COLOR_MAGENTA + TEXT_BOLD + "Categories:" + TEXT_COLOR_RESET)
    
    for idx, (category, games) in enumerate(game_categories.items()):
        stdscr.addstr(idx + 2, 2, f"{idx + 1}. {category}", curses.color_pair(1) if idx == selected_category_idx else curses.color_pair(2))
    
    stdscr.refresh()

def display_games(stdscr, selected_game_idx, selected_category):
    stdscr.clear()
    stdscr.addstr(0, 0, TEXT_BOLD + TEXT_COLOR_MAGENTA + f"'{selected_category}':" + TEXT_RESET)
    
    games = sorted(game_categories[selected_category])
    
    for idx, game in enumerate(games):
        stdscr.addstr(idx + 2, 2, f"{idx + 1}. {game}", curses.color_pair(1) if idx == selected_game_idx else curses.color_pair(2))
    
    stdscr.refresh()

def launch_game(game):
    # Function to launch a selected game
    clear_screen()
    print_header()
    print(TEXT_BOLD + TEXT_COLOR_MAGENTA + "=" * 50 + "\n\n"+ TEXT_RESET)
    display_center_text_with_delay(TEXT_BOLD + TEXT_COLOR_MAGENTA + " -> starting {}...\n\n".format(game) + TEXT_RESET)
    display_center_text(TEXT_BOLD + TEXT_COLOR_MAGENTA + " -> have fun! :-)\n\n".format(game) + TEXT_RESET)
    print_with_delay(TEXT_BOLD + TEXT_COLOR_GREEN + "ha" * 100 + "\n\n"+ TEXT_RESET)
    print(TEXT_BOLD + TEXT_COLOR_MAGENTA + "=" * 50 + "\n\n"+ TEXT_RESET)
    if game in game_commands:
        command = game_commands[game]
        os.system(command)
        clear_screen()
        print_header()
        print_with_delay(TEXT_BOLD + TEXT_COLOR_YELLOW +"I hope you had fun wasting your time playing {}!\n".format(game) + TEXT_RESET)
    else:
        clear_screen()
        print_header()
        print_with_delay(TEXT_COLOR_RED + TEXT_BOLD + "The Wizard says: Thou art a Fool! There is no command to launch {}!\n".format(game) + TEXT_RESET)
    input("\nPress Enter to continue...")
    display_categories()


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    selected_category_idx = 0
    selected_game_idx = 0
    
    while True:
        display_categories(stdscr, selected_category_idx)
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_DOWN:
            selected_category_idx = min(selected_category_idx + 1, len(game_categories) - 1)
        elif key == curses.KEY_UP:
            selected_category_idx = max(selected_category_idx - 1, 0)
        elif key == 10:  # Enter key
            selected_category = list(game_categories.keys())[selected_category_idx]
            
            while True:
                display_games(stdscr, selected_game_idx, selected_category)
                game_key = stdscr.getch()
                
                if game_key == ord('q'):
                    break
                elif game_key == ord('b'):
                    break
                elif game_key == curses.KEY_DOWN:
                    selected_game_idx = min(selected_game_idx + 1, len(game_categories[selected_category]) - 1)
                elif game_key == curses.KEY_UP:
                    selected_game_idx = max(selected_game_idx - 1, 0)
                elif game_key == 10:  # Enter key
                    selected_game = sorted(game_categories[selected_category])[selected_game_idx]
                    launch_game(selected_game)

if __name__ == "__main__":
    curses.wrapper(main)
