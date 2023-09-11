import json

# Load the JSON database
with open('daggerfall_potions.json', 'r') as json_file:
    data = json.load(json_file)

# Function to find which potions use a given ingredient
def find_potions_using_ingredient(ingredient_name):
    potions = []
    for recipe in data["recipes"]:
        if ingredient_name in recipe["ingredients"]:
            potions.append(recipe["potion_name"])
    return potions

# Function to find the ingredients used in a given potion
def find_ingredients_for_potion(potion_name):
    for recipe in data["recipes"]:
        if recipe["potion_name"] == potion_name:
            return recipe["ingredients"]
    return None

# User interface
while True:
    print("Daggerfall Potion App")
    print("1. Find potions using an ingredient")
    print("2. Find ingredients for a potion")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ingredient_name = input("Enter an ingredient name: ")
        potions = find_potions_using_ingredient(ingredient_name)
        if potions:
            print(f"Potions that use {ingredient_name}: {', '.join(potions)}")
        else:
            print(f"No potions use {ingredient_name}")

    elif choice == "2":
        potion_name = input("Enter a potion name: ")
        ingredients = find_ingredients_for_potion(potion_name)
        if ingredients:
            print(f"Ingredients for {potion_name}: {', '.join(ingredients)}")
        else:
            print(f"No information found for {potion_name}")

    elif choice == "3":
        break

