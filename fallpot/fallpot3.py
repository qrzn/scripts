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

# User interface to list items
def list_items(items, item_type):
    page = 1
    items_per_page = 10

    while True:
        print(f"\nList of {item_type} (Page {page}):")
        display_paginated_items(items, page, items_per_page)
        
        print("\nOptions:")
        print("1. Next Page")
        print("2. Previous Page")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            page += 1
        elif choice == "2":
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == "3":
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
            list_items(ingredient_names, "Ingredients")
        elif choice == "2":
            potions = database.get("potions", [])
            potion_names = [potion["category"] for potion in potions]
            list_items(potion_names, "Potions")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

