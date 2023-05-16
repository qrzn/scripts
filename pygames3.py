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

        self.category_label = tk.Label(self, text="Select a category:")
        self.category_label.pack(side="top")

        self.category_listbox = tk.Listbox(self)
        self.category_listbox.pack(side="left", fill="y")

        self.game_listbox = tk.Listbox(self)
        self.game_listbox.pack(side="left", fill="y")

        # Dictionary mapping categories to games
        self.games_by_category = {
                "DOS": ["Albion", "Caster of Magic", "Commander Keen", "Daggerfall", "Siedler 2"],
                "Wine": ["Arcanum", "Emperor", "Diablo II", "Stronghold", "Pharaoh", "Weltwunder", "Zeus"],
            "Steam": ["Game 2"],
            "Native": ["Game 2"],
            "Emulators": ["Game 2"],
        }

        # Add categories to the category listbox
        for category in self.games_by_category.keys():
            self.category_listbox.insert(tk.END, category)

        self.category_listbox.bind("<<ListboxSelect>>", self.update_game_list)

        self.launch_button = tk.Button(self, text="Launch Game", command=self.launch_game)
        self.launch_button.pack(side="bottom")

    def update_game_list(self, event):
        selected_category = self.category_listbox.get(tk.ACTIVE)
        # Clear the game listbox
        self.game_listbox.delete(0, tk.END)

        if selected_category in self.games_by_category:
            games = self.games_by_category[selected_category]
            # Sort the games alphabetically
            games.sort()

            # Add the sorted games to the game listbox
            for game in games:
                self.game_listbox.insert(tk.END, game)

    def launch_game(self):
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
root = tk.Tk()
root.geometry("400x300")  # Set the initial size of the GUI (width x height)
launcher = GameLauncher(master=root)
launcher.pack(fill="both", expand=True)  # Adjust the size of the frame to fill the available space
launcher.mainloop()

