import json

# Define the ingredients and their effects
ingredients = [
    {"name": "Rain Water", "effect": ["Chameleon Form"]},
    {"name": "Nectar", "effect": ["Chameleon Form", "Cure Disease"]},
    {"name": "Green Leaves", "effect": ["Chameleon Form"]},
    {"name": "Yellow Flowers", "effect": ["Chameleon Form"]},
    {"name": "Green Berries", "effect": ["Chameleon Form"]},
    {"name": "Red Berries", "effect": ["Chameleon Form"]},
    {"name": "Elixir Vitae", "effect": ["Chameleon Form", "Cure Disease", "Healing"]},
    {"name": "Fig", "effect": ["Cure Disease"]},
    {"name": "Big Tooth", "effect": ["Cure Disease"]},
    {"name": "Nymph's Hair", "effect": ["Cure Disease"]},
    {"name": "Ichor", "effect": ["Cure Poison", "Free Action"]},
    {"name": "Giant Scorpion Stinger", "effect": ["Cure Poison"]},
    {"name": "Small Tooth", "effect": ["Cure Poison"]},
    {"name": "Pearl", "effect": ["Cure Poison"]},
    {"name": "Spider's Venom", "effect": ["Free Action"]},
    {"name": "Twigs", "effect": ["Free Action"]},
    {"name": "Bamboo", "effect": ["Free Action"]},
    {"name": "Mercury", "effect": ["Healing"]},
    {"name": "Troll's Blood", "effect": ["Healing"]},
    {"name": "Pine Branch", "effect": ["Healing"]},
    {"name": "Unicorn Horn", "effect": ["Healing"]}
]

# Define the potion categories, variants, and their ingredients
potions = [
    {
        "category": "Chameleon Form",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Rain Water", "Nectar", "Green Leaves", "Yellow Flowers", "Green Berries"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Rain Water", "Nectar", "Green Leaves", "Yellow Flowers", "Red Berries"]
            },
            {
                "name": "Variant 3",
                "ingredients": ["Rain Water", "Nectar", "Green Leaves", "Yellow Flowers", "Green Berries", "Elixir Vitae"]
            }
        ]
    },
    {
        "category": "Cure Disease",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Elixir Vitae", "Fig", "Big Tooth"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Elixir Vitae", "Fig", "Nymph's Hair"]
            }
        ]
    },
    {
        "category": "Cure Poison",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Ichor", "Giant Scorpion Stinger", "Small Tooth", "Pearl"]
            }
        ]
    },
    {
        "category": "Free Action",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Ichor", "Spider's Venom", "Twigs", "Bamboo"]
            }
        ]
    },
    {
        "category": "Healing",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Elixir Vitae", "Red Berries", "Mercury", "Troll's Blood"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Pine Branch", "Red Berries", "Unicorn Horn"]
            }
        ]
    }
]

# Create the JSON database
database = {"ingredients": ingredients, "potions": potions}

# Write the JSON database to a file
with open("daggerfall_potions.json", "w") as json_file:
    json.dump(database, json_file, indent=2)

print("JSON database has been generated and saved as 'daggerfall_potions.json'.")

