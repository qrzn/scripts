import json

def generate_hexagrams():
    hexagrams = {}
    for i in range(64):
        hexagram = format(i, '06b')  # Convert the index to a 6-digit binary string
        hexagrams[hexagram] = {
            "hexagram": f"Hexagram {i+1}",
            "image": f"Image of Hexagram {i+1}",
            "judgment": f"Judgment of Hexagram {i+1}",
            "description": f"Description of Hexagram {i+1}"
        }
    return hexagrams

# Generate the hexagrams
all_hexagrams = generate_hexagrams()

# Save the hexagrams to a JSON file
with open("hexagrams.json", "w") as file:
    json.dump(all_hexagrams, file, indent=4)

print("Hexagrams JSON file generated successfully.")

