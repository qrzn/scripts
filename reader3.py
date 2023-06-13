import shutil
import time

def print_centered(line):
    # Get the terminal size
    terminal_size = shutil.get_terminal_size()

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

    # Print a new line after the line is printed
    print()

def print_with_delay(line):
    # Add a time delay for demonstration purposes
    time.sleep(0.5)
    print(line)

# Example usage
line = "Hello, world!"
print_centered(line)
