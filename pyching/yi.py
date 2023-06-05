import json
import random
import os
import textwrap

class Hexagram:
    def __init__(self, hexagram, image, judgment, description):
        self.hexagram = hexagram
        self.image = image
        self.judgment = judgment
        self.description = description

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_top_bar():
    clear_screen()

    print("-" * 50)
    print("{:^50}".format("Pythonian I Ching"))
    print("{:^50}".format("by qrzn"))
    print("-" * 50)

def generate_hexagram():
    hexagram = ""
    for _ in range(6):
        line = random.randint(6, 7)
        hexagram += str(line)
    return hexagram

def display_hexagram(hexagram):
    lines = []
    for line in hexagram:
        if line == '6':
            lines.append("-------")
        elif line == '7':
            lines.append("--- ---")
        elif line == '8':
            lines.append("---x---")
        elif line == '9':
            lines.append("---o---")
    
    print("Sequence:")
    for line in lines:
        print(line)

def interpret_hexagram(hexagram):
    # Load interpretations from the JSON file
    with open("int.json") as file:
        interpretations = json.load(file)
    
    interpretation_data = interpretations.get(hexagram)
    if interpretation_data:
        return Hexagram(
            interpretation_data["hexagram"],
            interpretation_data["image"],
            interpretation_data["judgment"],
            interpretation_data["description"]
        )
    else:
        return Hexagram(
            "Unknown Hexagram",
            "Unknown Image",
            "Unknown Judgment",
            "Unknown Description"
        )

# Function to prompt for a new reading or exit

def prompt_new_reading():
    print("\nPress 'Enter' for a new reading or 'q' to exit...")
    user_input = input()
    if user_input.lower() == "q":
        return False
    return True

# Main program execution

while True:

    # Display the top bar
    display_top_bar()

    # Generate a random hexagram
    random_hexagram = generate_hexagram()
    print("Hexagram:", random_hexagram)

    # Display the hexagram
    display_hexagram(random_hexagram)

    # Interpret the hexagram
    interpretation = interpret_hexagram(random_hexagram)
    print("Hexagram:", interpretation.hexagram)

    print("Image:")
    wrapped_image = textwrap.wrap(interpretation.image, width=60)
    for line in wrapped_image:
        print(line)

    print("Judgment:")
    wrapped_judgment = textwrap.wrap(interpretation.judgment, width=60)
    for line in wrapped_judgment:
        print(line)
    print("Description:")
    wrapped_description = textwrap.wrap(interpretation.description)
    for line in wrapped_description:
        print(line)
    
    #promt for a new reading or exit
    if not prompt_new_reading():
        break
