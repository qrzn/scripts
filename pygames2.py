import tkinter as tk
import os

class GameLauncher(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.game_label = tk.Label(self, text="Select a game to launch:")
        self.game_label.pack(side="top")

        self.game_listbox = tk.Listbox(self)
        self.game_listbox.pack(side="top")

        # List of games
        games = ["Albion", "Arcanum", "Caster of Magic", "Commander Keen", "Darklands", "Daggerfall", "Daggerfall - Unity", "Emperor", "Exult", "Factorio", "Master of Orion", "Master of Orion 2", "Morrowind", "Pharaoh", "Siedler 2", "Stardew Valley", "Ultima Underworld II", "Widelands", "Zeus"]

        # Sort the games alphabetically
        games.sort()

        # Add the sorted games to the listbox
        for game in games:
            self.game_listbox.insert(tk.END, game)

        self.launch_button = tk.Button(self, text="Launch Game", command=self.launch_game)
        self.launch_button.pack(side="bottom")

    def launch_game(self):
        selected_game = self.game_listbox.get(tk.ACTIVE)
        # Launch the game using the appropriate command
        if selected_game == "Albion":
            os.system("dosbox -conf ~/.dosbox/albion.conf")
        elif selected_game == "Arcanum":
            os.system("cd ~/Spiele/Arcanum/ && wine Arcanum.exe")
        elif selected_game == "Der erste Kaiser":
            os.system("cd ~/Spiele/emperor/ && wine Emperor.exe")
        elif selected_game == "Daggerfall Unity":
            os.system("cd ~/Spiele/dfu && ./DaggerfallUnity.x86_64")
        elif selected_game == "Daggerfall":
            os.system("dosbox -conf ~/.dosbox/fall.conf")
        elif selected_game == "Commander Keen":
            os.system("dosbox -conf ~/.dosbox/keen.conf")
        elif selected_game == "Factorio":
            os.system("cd ~/Spiele/factorio/bin/x64 && ./factorio")
        elif selected_game == "Exult":
            os.system("exult")
        elif selected_game == "Caster of Magic":
            os.system("dosbox -conf ~/.dosbox/com.conf")

root = tk.Tk()
launcher = GameLauncher(master=root)
launcher.mainloop()

