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

# Display a paginated list of items
def display_paginated_items(items, page, items_per_page):
    start_idx = (page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, len(items))
    
    print(f"Page {page}:")
    for idx in range(start_idx, end_idx):
        print(f"{idx + 1}. {items[idx]}")

# Display ingredients for a potion
def display_potion_ingredients(potion_name, database):
    potions = database.get("potions", [])
    for potion in potions:
        if potion["category"] == potion_name:
            print(f"Ingredients for {potion_name}:")
            for idx, variant in enumerate(potion['variants'], start=1):
                print(f"{idx}. {variant['name']} - {', '.join(variant['ingredients'])}")

# User interface to list items
def list_items(items, item_type, database):
    page = 1
    items_per_page = 10

    while True:
        print(f"\nList of {item_type} (Page {page}):")
        display_paginated_items(items, page, items_per_page)
        
        print("\nOptions:")
        print("1. Next Page")
        print("2. Previous Page")
        if item_type == "Potions":
            print("3. View Potion Ingredients by Number")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            page += 1
        elif choice == "2":
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == "3" and item_type == "Potions":
            try:
                potion_number = int(input("Enter the number of the potion to view its ingredients: ")) - 1
                if 0 <= potion_number < len(items):
                    potion_name = items[potion_number]
                    display_potion_ingredients(potion_name, database)
                else:
                    print("Invalid potion number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Main user interface
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
            ingredients = database.get("ingredients", [])
            ingredient_names = [ingredient["name"] for ingredient in ingredients]
            list_items(ingredient_names, "Ingredients", database)
        elif choice == "2":
            potions = database.get("potions", [])
            potion_names = [potion["category"] for potion in potions]
            list_items(potion_names, "Potions", database)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

