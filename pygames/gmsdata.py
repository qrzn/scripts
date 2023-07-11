import json
import time

def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

# Dictionary to hold game categories and their associated games
game_categories = {
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
        "Ultima 4-6",
        "Ultima Underworld",
        "Veil of Darkness",
        "Sakura Dungeon",
        "Legend of Grimrock",
        ],
    "Strategy": [
        "Centurion",
        "Dawn of War",
        "Dungeon Keeper II",
        "Factorio",
        "Emperor",
        "Return to the Roots",
        "Siedler 2 modded",
        "Siedler 2",
        "Stronghold",
        "Stronghold Crusader",
        "Stronghold Crusader Extreme",
        "Pharaoh",
        "War Wind",
        "Weltwunder",
        "XCOM 2",
        "Zeus",
        ],
    "Action": [
        "Apotheon",
        "CrossCode",
        "Commander Keen",
        "Lost Ruins",
        "Duke Nukem 3D",
        "Half-Life",
        "Pirates!",
        "Quake",
        ],
    "Tools": [
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
        "Civilization V",
        "Civilization VI",
        "Stellaris",
        "Ascendancy",
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
        "Kerbal Space Program",
        "Terraria",
        ],
    "Emulators": [
        "RetroArch", 
        "ScummVM",
        "Dosbox",
        "Steam"
        ],
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
    "Siedler 2 modded": "dosbox -conf ~/.dosbox/s2.conf",
    "Siedler 2": "dosbox -conf ~/.dosbox/siedler2.conf",
    "Master of Orion": "dosbox -conf ~/.dosbox/moo.conf",
    "Master of Orion II - Battle at Antares": "dosbox -conf ~/.dosbox/moo2.conf",
    "Master of Magic": "dosbox -conf ~/.dosbox/mom.conf",
    "Ultima 4-6": "dosbox -conf ~/.dosbox/ultima.conf",
    "Ultima Underworld": "dosbox -conf ~/.dosbox/uuw.conf",
    "Pirates!": "dosbox -conf ~/.dosbox/pirates.conf",
    "Quake": "dosbox -conf ~/.dosbox/quake.conf",
    "Veil of Darkness": "dosbox -conf ~/.dosbox/veil.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    # wine
    "Arcanum": "cd ~/Spiele/wine/Arcanum/ && wine Arcanum.exe",
    "Emperor": "cd ~/Spiele/wine/emperor/ && wine Emperor.exe",
    "Diablo II": "cd ~/Spiele/wine/diablo2/ && wine Game.exe",
    "Fallout": "cd ~/Spiele/wine/fallout/ && wine FALLOUTW.exe",
    "Fallout 2": "cd ~/Spiele/wine/fallout2/ && wine fallout2.exe",
    "Fallout New Vegas": "cd ~/Spiele/wine/fnv/ && wine nvse_loader.exe",
    "Dungeon Keeper II": "cd ~/Spiele/wine/dk2/ && wine DKII-DX.exe",
    "Galactic Civilizations II": "cd ~/Spiele/wine/galciv2/ && wine Game.exe",
    "Stronghold": "cd ~/Spiele/wine/stronghold/ && wine Stronghold.exe",
    "Stronghold Crusader": "cd ~/Spiele/wine/strongholdchd/ && wine shc.exe",
    "Stronghold Crusader Extreme": "cd ~/Spiele/wine/strongholdchd/ && wine shc.exe",
    "Pharaoh": "cd ~/Spiele/wine/pharaoh/ && wine Pharaoh.exe",
    "War Wind": "cd ~/Spiele/wine/warwind/ && wine WW.exe",
    "Weltwunder": "cd ~/Spiele/wine/c4/ && wine Game.exe",
    "Zeus": "cd ~/Spiele/wine/zeus/ && wine Zeus.exe",
    # Native
    "Daggerfall Unity": "~/Spiele/dfu/DaggerfallUnity.x86_64",
    "Don't Starve": "~/Spiele/dontstarve/start.sh",
    "Exult": "exult",
    "Factorio": "~/Spiele/factorio/bin/x64/factorio",
    "Return to the Roots": "sh ~/Spiele/native/rttr/bin/rttr.sh",
    "Starbound": "~/Spiele/starbound/start.sh",
    "Stardew Valley": "~/Spiele/stardew/start.sh",
    "OpenMW": "openmw-launcher",
    "Widelands": "widelands",
    "The Ur-Quan Masters": "uqm",
    "Valhalla": "~/Spiele/valhalla/start.sh",
    # Emulators
    "RetroArch": "retroarch",
    "ScummVM": "scummvm",
    "Dosbox": "dosbox",
    "Steam": "steam",
    # Steam
    "Stellaris": "steam steam://rungameid/281990",
    "Civilization V": "steam steam://rungameid/8930",
    "Civilization VI": "steam steam://rungameid/289070",
    "Lost Ruins": "steam steam://rungameid/1306630",
    "Apotheon": "steam steam://rungameid/208750",
    "Kerbal Space Program": "steam steam://rungameid/281990",
    "X3 - Terran Conflict": "steam steam://rungameid/2820",
    "Dawn of War": "steam steam://rungameid/9450",
    "XCOM 2": "steam steam://rungameid/268500",
    "CrossCode": "steam steam://rungameid/368340",
    "Terraria": "steam steam://rungameid/105600",
    "Sakura Dungeon": "steam steam://rungameid/407330",
    "Legend of Grimrock": "steam steam://rungameid/207170",
}

# Creating a dictionary to hold both categories and commands
data = {
    "categories": game_categories,
    "commands": game_commands
}

# Writing the dictionary to a JSON file
with open("game_data.json", "w") as file:
    json.dump(data, file)

print_with_delay("Game Data JSON file generated successfully.")
