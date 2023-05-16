import tkinter as tk
import os

class GameLauncher(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create label for game selection
        self.game_label = tk.Label(self, text="Select a game to launch:")
        self.game_label.pack(side="top")

        # Create label for category selection
        self.category_label = tk.Label(self, text="Select a category:")
        self.category_label.pack(side="top")

        # Create listbox for categories
        self.category_listbox = tk.Listbox(self)
        self.category_listbox.pack(side="left", fill="y")

        # Create listbox for games
        self.game_listbox = tk.Listbox(self)
        self.game_listbox.pack(side="left", fill="y")

        # Dictionary mapping categories to games
        self.games_by_category = self.generate_categories()

        # Populate the category listbox with categories
        for category in self.games_by_category.keys():
            self.category_listbox.insert(tk.END, category)

        # Bind the update_game_list method to the category listbox selection event
        self.category_listbox.bind("<<ListboxSelect>>", self.update_game_list)

        # Create launch button
        self.launch_button = tk.Button(self, text="Launch Game", command=self.launch_game)
        self.launch_button.pack(side="bottom")

    def generate_categories(self):
        # Generate categories dynamically based on game data
        games_by_category = {}

        # Add your game data and their categories dynamically
        games_data = {
            "Game 1": "Category 1",
            "Game 2": "Category 2",
            "Game 3": "Category 1",
            "Game 4": "Category 2",
        }

        for game, category in games_data.items():
            if category in games_by_category:
                # Append game to an existing category
                games_by_category[category].append(game)
            else:
                # Create a new category with the game
                games_by_category[category] = [game]

        return games_by_category

    def update_game_list(self, event):
        # Update the game listbox based on the selected category
        selected_category = self.category_listbox.get(tk.ACTIVE)
        self.game_listbox.delete(0, tk.END)  # Clear the game listbox

        if selected_category in self.games_by_category:
            games = self.games_by_category[selected_category]
            games.sort()  # Sort the games alphabetically
            for game in games:
                self.game_listbox.insert(tk.END, game)

    def launch_game(self):
        # Launch the selected game
        selected_game = self.game_listbox.get(tk.ACTIVE)
        if selected_game == "Game 1":
            os.system("path/to/game1.exe")
        elif selected_game == "Game 2":
            os.system("path/to/game2.exe")
        elif selected_game == "Game 3":
            os.system("path/to/game3.exe")
        elif selected_game == "Game 4":
            os.system("path/to/game4.exe")

root = tk.Tk()
root.geometry("400x300")  # Set the initial size of the GUI (width x height)
launcher = GameLauncher(master=root)
launcher.pack(fill="both", expand=True)  # Adjust the size of the frame to fill the available space
launcher.mainloop()

