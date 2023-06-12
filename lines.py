import time

def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

# Example usage
text = "Hello, World!"
print_with_delay(text)
