import time

def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

# Example usage: Print "Choice:" with delay
prompt = "Choice: "
print_with_delay(prompt)

user_input = input()
