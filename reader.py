import os
import time
import shutil

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')

def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

def print_centered(text):
    # Get the terminal size
    terminal_size = shutil.get_terminal_size()

    # Calculate the number of spaces needed for horizontal centering
    spaces = (terminal_size.columns - len(text)) // 2

    # Calculate the number of lines needed for vertical centering
    lines = (terminal_size.lines - 1) // 2

    # Clear the screen
    clear_screen()

    # Print empty lines for vertical centering
    for _ in range(lines):
        print()

    # Print spaces for horizontal centering
    print(' ' * spaces, end='')

    # Print the text with a time delay
    print_with_delay(text)

# Example usage: Read text from external .txt file
file_path = 'text.txt'
with open(file_path, 'r') as file:
    text = file.read()
    print_centered(text)
