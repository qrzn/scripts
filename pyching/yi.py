import json
import random
import os

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
    top_bar = "========== pyching =========="
    print(top_bar)

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
    
    print("Hexagram:")
    for line in lines:
        print(line)

def interpret_hexagram(hexagram):
    # Load interpretations from the JSON file
    with open("hexagrams.json") as file:
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

# Display the top bar
display_top_bar()

# Generate a random hexagram
random_hexagram = generate_hexagram()
print("Random Hexagram:", random_hexagram)

# Display the hexagram
display_hexagram(random_hexagram)

# Interpret the hexagram
interpretation = interpret_hexagram(random_hexagram)
print("Hexagram:", interpretation.hexagram)
print("Image:", interpretation.image)
print("Judgment:", interpretation.judgment)
print("Description:", interpretation.description)

