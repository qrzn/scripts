import json

# Load the JSON database
def load_database():
    try:
        with open('daggerfall_potions.json', 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print("JSON database 'daggerfall_potions.json' not found.")
        return None

# Display a list of all ingredients
def list_ingredients(database):
    ingredients = database.get("ingredients", [])
    ingredients.sort(key=lambda x: x["name"]) # Sort ingredients alphabetically
    print("List of Ingredients:")
    for idx, ingredient in enumerate(ingredients, start=1):
        print(f"{idx}. {ingredient['name']} - Effects: {', '.join(ingredient['effect'])}")

# Display a list of all potions and their variants
def list_potions(database):
    potions = database.get("potions", [])
    print("List of Potions:")
    for potion in potions:
        print(f"- {potion['category']}:")
        for variant in potion['variants']:
            print(f"  - {variant['name']} - Ingredients: {', '.join(variant['ingredients'])}")

# User interface
def main():
    database = load_database()
    if not database:
        return

    while True:
        print("\nDaggerfall Potion App")
        print("1. List Ingredients")
        print("2. List Potions")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_ingredients(database)
        elif choice == "2":
            list_potions(database)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

