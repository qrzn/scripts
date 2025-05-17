# NOTE MUTATION ENGINE — DIGITAL GUI PLATFORM (SCFSR-Aux-2)

import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import json

class Node:
    def __init__(self, label, mutation_level=0):
        self.label = label
        self.children = []
        self.mutation_level = mutation_level

    def mutate(self):
        mutation_type = random.choice(["invert", "contradict", "emerge", "erase"])
        self.label += f" ↻{mutation_type}"
        self.mutation_level += 1
        if mutation_type == "erase":
            self.children = []
        elif mutation_type == "emerge":
            new_node = Node(f"{self.label}-child", 0)
            self.children.append(new_node)

class NoteMutationEngine:
    def __init__(self, master):
        self.master = master
        self.master.title("Note Mutation Engine — SCFSR Platform")
        self.tree = Node("ROOT")

        self.canvas = tk.Canvas(master, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.toolbar = tk.Frame(master, bg="gray20")
        self.toolbar.pack(fill=tk.X)

        tk.Button(self.toolbar, text="Mutate", command=self.mutate_node).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Export", command=self.export_structure).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Reset", command=self.reset_tree).pack(side=tk.LEFT)

        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")
        self._draw_node(self.tree, 400, 20, 200)

    def _draw_node(self, node, x, y, x_offset):
        color = f"#{min(255, node.mutation_level*30):02x}ff{255 - min(255, node.mutation_level*30):02x}"
        self.canvas.create_text(x, y, text=node.label, fill=color, font=("Courier", 10, "bold"))
        for i, child in enumerate(node.children):
            child_x = x - x_offset + (i * 60)
            child_y = y + 60
            self.canvas.create_line(x, y + 10, child_x, child_y - 10, fill="white")
            self._draw_node(child, child_x, child_y, max(50, x_offset // 2))

    def mutate_node(self):
        path = simpledialog.askstring("Mutate", "Enter node path (e.g. 0.1.2):")
        if path is None:
            return
        try:
            node = self._get_node_by_path(path)
            node.mutate()
            self.draw_tree()
        except Exception:
            messagebox.showerror("Error", "Invalid path.")

    def _get_node_by_path(self, path):
        indices = list(map(int, path.strip().split(".")))
        node = self.tree
        for i in indices:
            node = node.children[i]
        return node

    def export_structure(self):
        def serialize(node):
            return {
                "label": node.label,
                "mutation_level": node.mutation_level,
                "children": [serialize(child) for child in node.children]
            }
        data = serialize(self.tree)
        with open("note_structure.json", "w") as f:
            json.dump(data, f, indent=2)
        messagebox.showinfo("Exported", "Structure saved to note_structure.json")

    def reset_tree(self):
        if messagebox.askyesno("Confirm Reset", "Erase all mutations and reset?"):
            self.tree = Node("ROOT")
            self.draw_tree()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteMutationEngine(root)
    root.mainloop()
