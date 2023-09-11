import json

# Define the ingredients and their effects
ingredients = [
    {"name": "Rain Water", "effect": ["Chameleon Form", "Invisibility (Normal)"]},
    {"name": "Nectar", "effect": ["Chameleon Form", "Cure Disease", "Invisibility (Normal)", "Levitation"]},
    {"name": "Green Leaves", "effect": ["Chameleon Form"]},
    {"name": "Yellow Flowers", "effect": ["Chameleon Form"]},
    {"name": "Green Berries", "effect": ["Chameleon Form"]},
    {"name": "Red Berries", "effect": ["Chameleon Form"]},
    {"name": "Elixir Vitae", "effect": ["Chameleon Form", "Cure Disease", "Healing", "Purification (Cure Disease)", "Restore Power"]},
    {"name": "Fig", "effect": ["Cure Disease", "Purification (Cure Disease)"]},
    {"name": "Big Tooth", "effect": ["Cure Disease", "Purification (Cure Disease)"]},
    {"name": "Nymph's Hair", "effect": ["Cure Disease"]},
    {"name": "Ichor", "effect": ["Cure Poison", "Free Action", "Resist Fire", "Resist Frost", "Resist Shock", "Resist Poison"]},
    {"name": "Giant Scorpion Stinger", "effect": ["Cure Poison"]},
    {"name": "Small Tooth", "effect": ["Cure Poison", "Purification (Cure Disease)"]},
    {"name": "Pearl", "effect": ["Cure Poison", "Purification (Cure Disease)"]},
    {"name": "Spider's Venom", "effect": ["Free Action", "Resist Shock"]},
    {"name": "Twigs", "effect": ["Free Action", "Resist Shock"]},
    {"name": "Bamboo", "effect": ["Free Action"]},
    {"name": "Mercury", "effect": ["Healing", "Purification (Cure Disease)"]},
    {"name": "Troll's Blood", "effect": ["Healing"]},
    {"name": "Pine Branch", "effect": ["Healing", "Purification (Cure Disease)"]},
    {"name": "Unicorn Horn", "effect": ["Healing", "Heal True", "Purification (Cure Disease)"]},
    {"name": "Yellow Berries", "effect": ["Heal True"]},
    {"name": "Ectoplasm", "effect": ["Invisibility (Normal)", "Levitation", "Purification (Cure Disease)"]},
    {"name": "Diamond", "effect": ["Invisibility (Normal)", "Purification (Cure Disease)"]},
    {"name": "Mummy Wrappings", "effect": ["Purification (Cure Disease)"]},
    {"name": "Amber", "effect": ["Resist Fire", "Slow Falling"]},
    {"name": "Red Flowers", "effect": ["Resist Fire"]},
    {"name": "Fairy Dragon Scales", "effect": ["Resist Fire"]},
    {"name": "Cactus", "effect": ["Resist Fire"]},
    {"name": "Turquoise", "effect": ["Resist Frost"]},
    {"name": "White Rose", "effect": ["Resist Frost"]},
    {"name": "Lodestone", "effect": ["Resist Shock", "Restore Power"]},
    {"name": "Snake Venom", "effect": ["Resist Poison"]},
    {"name": "Golden Poppy", "effect": ["Resist Poison"]},
    {"name": "Silver", "effect": ["Restore Power"]},
    {"name": "Werewolf's Blood", "effect": ["Restore Power"]},
    {"name": "Saint's Hair", "effect": ["Restore Power"]},
    {"name": "Malachite", "effect": ["Shadow Form", "Invisibility (Normal)"]},
    {"name": "Pure Water", "effect": ["Levitation", "Water Breathing", "Water Walking"]},
    {"name": "Aloe", "effect": ["Slow Falling", "Slow Falling"]},
    {"name": "Gingko Leaves", "effect": ["Slow Falling"]},
    {"name": "Ivory", "effect": ["Water Breathing"]},
    {"name": "Palm", "effect": ["Water Walking"]},
    {"name": "Yellow Rose", "effect": ["Water Walking"]},
    {"name": "Sulphur", "effect": ["Water Walking"]}
]

# Define the potions, variants, and their ingredients
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
    },
    {
        "category": "Heal True",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Elixir Vitae", "Red Berries", "Pine Branch", "Unicorn Horn"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Elixir Vitae", "Yellow Berries", "Green Berries", "Unicorn Horn"]
            }
        ]
    },
    {
        "category": "Invisibility (Normal)",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Rain Water", "Nectar", "Ectoplasm", "Diamond"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Rain Water", "Nectar", "Malachite", "Black Rose"]
            }
        ]
    },
    {
        "category": "Levitation",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Pure Water", "Nectar", "Ectoplasm"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Orc's Blood", "Pure Water", "Nectar", "Ectoplasm"]
            }
        ]
    },
    {
        "category": "Orc Strength",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Orc's Blood", "Iron", "Rain Water"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Nectar", "Iron", "Rain Water", "Elixir Vitae"]
            }
        ]
    },
    {
        "category": "Purification (Cure Disease)",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Elixir Vitae", "Nectar", "Rain Water", "Fig", "Big Tooth", "Ectoplasm", "Diamond", "Mummy Wrappings"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Elixir Vitae", "Nectar", "Rain Water", "Fig", "Big Tooth", "Ectoplasm", "Diamond", "Mummy Wrappings", "Elixir Vitae"]
            }
        ]
    },
    {
        "category": "Resist Fire",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Ichor", "Amber", "Red Flowers", "Fairy Dragon Scales", "Cactus"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Ichor", "Red Flowers", "Fairy Dragon Scales", "Cactus"]
            }
        ]
    },
    {
        "category": "Resist Frost",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Ichor", "Turquoise", "Pine Branch", "White Rose"]
            }
        ]
    },
    {
        "category": "Resist Shock",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Ichor", "Lodestone", "Red Berries"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Ichor", "Lodestone", "Yellow Berries"]
            },
            {
                "name": "Variant 3",
                "ingredients": ["Ichor", "Spider's Venom", "Twigs", "Bamboo"]
            }
        ]
    },
    {
        "category": "Resist Poison",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Ichor", "Snake Venom", "Golden Poppy"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Nectar", "Snake Venom", "Golden Poppy"]
            }
        ]
    },
    {
        "category": "Restore Power",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Nectar", "Silver", "Werewolf's Blood", "Lodestone"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Nectar", "Silver", "Werewolf's Blood", "Saint's Hair"]
            }
        ]
    },
    {
        "category": "Shadow Form",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Rain Water", "Nectar", "Malachite", "Black Rose"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Pure Water", "Nectar", "Malachite", "Black Rose"]
            }
        ]
    },
    {
        "category": "Slow Falling",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Pure Water", "Aloe", "Gingko Leaves"]
            },
            {
                "name": "Variant 2",
                "ingredients": ["Ichor", "Amber", "Aloe", "Gingko Leaves"]
            }
        ]
    },
    {
        "category": "Water Breathing",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Rain Water", "Elixir Vitae", "Ivory"]
            }
        ]
    },
    {
        "category": "Water Walking",
        "variants": [
            {
                "name": "Variant 1",
                "ingredients": ["Pure Water", "Palm", "Yellow Rose", "Sulphur"]
            }
        ]
    },
]

# Create the JSON database
database = {"ingredients": ingredients, "potions": potions}

# Write the JSON database to a file
with open("daggerfall_potions.json", "w") as json_file:
    json.dump(database, json_file, indent=2)

print("JSON database has been generated and saved as 'daggerfall_potions.json'.")

