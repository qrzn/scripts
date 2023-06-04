import os

# Dictionary to hold game categories and their associated games
game_categories = {
    "DOS": [
        "Albion",
        "Arena",
        "Ascendancy",
        "Centurion",
        "Civilization",
        "Caster of Magic",
        "Commander Keen", 
        "Daggerfall", 
        "Darklands", 
        "Duke Nukem 3D", 
        "Dune II", 
        "Master of Magic", 
        "Master of Orion", 
        "Master of Orion II - Battle at Antares", 
        "Pirates!", 
        "Ultima", 
        "Quake", 
        "Siedler 2", 
        "Shadow Warrior", 
        "Ultima", 
        "Ultima Underworld",
        "Veil of Darkness", 
        "Zeliard"
        ],
    "RPG": [
        "Albion",
        "Arena",
        "Arcanum",
        "Daggerfall",
        "Daggerfall Unity",
        "Darklands",
        "Diablo II",
        "Exult",
        "Fallout",
        "Fallout 2",
        "Fallout New Vegas",
        "OpenMW",
        "Darklands",
        "Ultima 4-6",
        "Ultima Underworld",
        "Veil of Darkness",
        ],
    "Strategy": [
        "Ascendancy",
        "Civilization",
        "Centurion",
        "Dungeon Keeper II",
        "Factorio",
        "Emperor",
        "Caster of Magic",
        "Master of Magic",
        "Master of Orion",
        "Master of Orion II - Battle at Antares",
        "Siedler 2",
        "Stronghold",
        "Stronghold Crusader",
        "Pharaoh",
        "War Wind",
        "Weltwunder",
        "Zeus",
        ],
    "Action": [
        "Albion",
        "Arena",
        "Commander Keen",
        "Duke Nukem 3D",
        "Half-Life",
        "Pirates!",
        "Quake",
        ],
    "4X": [
        "Civilization",
        "Master of Magic",
        "Master of Orion",
        "Caster of Magic",
        "Master of Orion II - Battle at Antares",

        ],
    "Steam": [
        "Civilization",
        "Master of Magic",
        "Master of Orion",
        "Caster of Magic",
        "Master of Orion II - Battle at Antares",

        ],
    "Indie": [
        "Don't Starve",
        "Factorio",
        "Starbound",
        "Stardew Valley",
        ],
    "Wine": [
        "Arcanum", 
        "Emperor", 
        "Diablo II", 
        "Dungeon Keeper II", 
        "Fallout", 
        "Fallout 2", 
        "Fallout New Vegas", 
        "Galactic Civilizations II", 
        "Stronghold", 
        "Stronghold Crusader", 
        "Pharaoh", 
        "War Wind", 
        "Weltwunder", 
        "Zeus"
        ],
    "Native": [
        "Exult", 
        "Factorio", 
        "Don't Starve", 
        "Daggerfall Unity", 
        "Return to the Roots", 
        "OpenMW", 
        "Stardew Valley", 
        "Starbound", 
        "The Ur-Quan Masters",
        "Widelands",
        "Valhalla"
        ],
    "Emulators": ["RetroArch", "ScummVM"],
}

# Dictionary to hold game commands
game_commands = {
    # DOS
    "Albion": "dosbox -conf ~/.dosbox/albion.conf",
    "Arena": "dosbox -conf ~/.dosbox/arena.conf",
    "Caster of Magic": "dosbox -conf ~/.dosbox/com.conf",
    "Commander Keen": "dosbox -conf ~/.dosbox/keen.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    "Dune 2": "dosbox -conf ~/.dosbox/dune2.conf",
    "Siedler 2": "dosbox -conf ~/.dosbox/s2.conf",
    "Master of Orion": "dosbox -conf ~/.dosbox/moo.conf",
    "Master of Magic": "dosbox -conf ~/.dosbox/mom.conf",
    "Ultima 4-6": "dosbox -conf ~/.dosbox/ultima.conf",
    "Ultima Underworld": "dosbox -conf ~/.dosbox/uuw.conf",
    "Pirates!": "dosbox -conf ~/.dosbox/pirates.conf",
    "Quake": "dosbox -conf ~/.dosbox/quake.conf",
    "Veil of Darkness": "dosbox -conf ~/.dosbox/veil.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    # wine
    "Arcanum": "wine ~/Spiele/wine/Arcanum/Arcanum.exe",
    "Emperor": "wine ~/Spiele/wine/emperor/Emperor.exe",
    "Diablo II": "wine ~/Spiele/wine/diablo2/Game.exe",
    "Fallout": "wine ~/Spiele/wine/fallout/FALLOUTW.exe",
    "Fallout 2": "wine ~/Spiele/wine/fallout2/fallout2.exe",
    "Dungeon Keeper II": "wine ~/Spiele/wine/dk2/DKII-DX.exe",
    "Galactic Civilizations II": "wine ~/Spiele/wine/galciv2/Game.exe",
    "Stronghold": "wine ~/Spiele/wine/stronghold/Stronghold.exe",
    "Stronghold Crusader": "wine ~/Spiele/wine/stronghold/Stronghold.exe",
    "Pharaoh": "wine ~/Spiele/wine/pharaoh/Pharaoh.exe",
    "War Wind": "wine ~/Spiele/wine/warwind/WW.exe",
    "Weltwunder": "wine ~/Spiele/wine/c4/Game.exe",
    "Zeus": "wine ~/Spiele/wine/zeus/Zeus.exe",
    # Native
    "Daggerfall Unity": "~/Spiele/dfu/DaggerfallUnity.x86_64",
    "Don't Starve": "~/Spiele/dontstarve/start.sh",
    "Exult": "exult",
    "Factorio": "~/Spiele/factorio/bin/x64/factorio",
    "Starbound": "~/Spiele/starbound/start.sh",
    "Stardew Valley": "~/Spiele/stardew/start.sh",
    "OpenMW": "openmw-launcher",
    "Widelands": "widelands",
    "The Ur-Quan Masters": "uqm",
    "Valhalla": "~/Spiele/valhalla/start.sh",
    # Emulators
    "RetroArch": "retroarch",
    "ScummVM": "scummvm",
}

def header():
    print("-" * 50)
    print("{:^50}".format("Game Serpent Wizard 1.0"))
    print("{:^50}".format("by qrzn"))
    print("-" * 50)

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_categories():
    # Function to display available game categories
    clear_screen()
    header()
    print("Choose Thy Categorie:")
    index = 1
    for category in sorted(game_categories.keys()):
        print("{}. {}".format(index, category))
        index += 1
    print()

def display_games(category):
    # Function to display games in a specific category
    clear_screen()
    header()
    print("Games in the '{}' Category:".format(category))
    games = sorted(game_categories[category])
    index = 1
    for game in games:
        print("{}. {}".format(index, game))
        index += 1
    print()

def launch_game(game):
    # Function to launch a selected game
    clear_screen()
    print("Launching {}...".format(game))
    if game in game_commands:
        command = game_commands[game]
        os.system(command)
        print("Enjoy the game!")
    else:
        print("No command found to launch the game.")
    input("Press Enter to continue...")
    display_categories()

# Main game launcher loop
while True:
    display_categories()
    category_choice = input("Choose Thy Categorie [1-9] (or 'q' to exit): ")
    if category_choice == "q":
        break
    elif category_choice.isdigit():
        category_choice = int(category_choice)
        if 1 <= category_choice <= len(game_categories):
            categories = sorted(game_categories.keys())
            selected_category = categories[category_choice - 1]
            display_games(selected_category)
            game_choice = input("Choose Thy Game number (or go 'b'ack or 'q'uit): ")
            if game_choice == "b":
                continue
            elif game_choice == "q":
                break
            elif game_choice.isdigit():
                game_choice = int(game_choice)
                games = sorted(game_categories[selected_category])
                if 1 <= game_choice <= len(games):
                    selected_game = games[game_choice - 1]
                    launch_game(selected_game)
                else:
                    print("Invalid game selection!")
                    input("Press Enter to continue...")
            else:
                print("Invalid input!")
                input("Press Enter to continue...")
        else:
            print("Invalid category selection!")
            input("Press Enter to continue...")
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
