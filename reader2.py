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

def print_centered(lines):
    # Get the terminal size
    terminal_size = shutil.get_terminal_size()

    # Clear the screen
    clear_screen()

    for line in lines:
        # Calculate the number of spaces needed for horizontal centering
        spaces = (terminal_size.columns - len(line)) // 2

        # Calculate the number of lines needed for vertical centering
        lines = (terminal_size.lines - 1) // 2

        # Print empty lines for vertical centering
        for _ in range(lines):
            print()

        # Print spaces for horizontal centering
        print(' ' * spaces, end='')

        # Print the line with a time delay
        print_with_delay(line)

        # Print a new line after each line is printed
        print()

# Example usage: Read lines from external .txt file
file_path = 'text.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print_centered(lines)

