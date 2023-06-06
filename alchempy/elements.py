import json

# Define the elements and combinations
elements = {
    'fire': {
        'properties': ['hot', 'bright'],
        'combinations': ['fire + water = steam', 'fire + earth = lava']
    },
    'water': {
        'properties': ['wet', 'cool'],
        'combinations': ['water + earth = mud', 'water + fire = steam']
    },
    'earth': {
        'properties': ['solid', 'grounded'],
        'combinations': ['earth + water = mud', 'earth + fire = lava']
    },
    'air': {
        'properties': ['light', 'gaseous'],
        'combinations': ['air + fire = smoke', 'air + water = mist']
    },
}

# Save the elements dictionary to a JSON file
with open('elements.json', 'w') as file:
    json.dump(elements, file)

