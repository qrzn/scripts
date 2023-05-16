import tkinter as tk
import os

dosbox = "$HOME/.dosbox/"
game= "$HOME/Spiele"

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

        self.launch_button = tk.Button(self, text="Launch Game", command=self.launch_game)
        self.launch_button.pack(side="bottom")

        # Add games to the listbox
        self.game_listbox.insert(tk.END, "Albion")
        self.game_listbox.insert(tk.END, "Arcanum")
        self.game_listbox.insert(tk.END, "Der erste Kaiser")
        self.game_listbox.insert(tk.END, "Daggerfall Unity")
        self.game_listbox.insert(tk.END, "Daggerfall")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")
        self.game_listbox.insert(tk.END, "Widelands")

    def launch_game(self):
        # Get the selected game from the listbox
        selected_game = self.game_listbox.get(tk.ACTIVE)

        # Launch the game using the appropriate command
        if selected_game == "Albion":
            os.system("dosbox -conf ~/dosbox/albion.conf")
        elif selected_game == "Arcanum":
            os.system("cd ~/Spiele/Arcanum/ && wine Arcanum.exe")
        elif selected_game == "Der erste Kaiser":
            os.system("cd ~/Spiele/emperor/ && wine Emperor.exe")
        elif selected_game == "Daggerfall Unity":
            os.system("cd ~/Spiele/dfu && ./DaggerfallUnity.x86_64")
        elif selected_game == "Widelands":
            os.system("widelands")
        elif selected_game == "Widelands":
            os.system("widelands")
        elif selected_game == "Widelands":
            os.system("widelands")
        elif selected_game == "Widelands":
            os.system("widelands")
        elif selected_game == "Widelands":
            os.system("widelands")
# Create the GUI
root = tk.Tk()
launcher = GameLauncher(master=root)
launcher.mainloop()
