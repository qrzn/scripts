import matplotlib.pyplot as plt
import networkx as nx
import random
import os
from matplotlib.animation import FuncAnimation

# === CONFIGURATION ===
GENERATIONS = 6
INITIAL_POPULATION = 1
BRANCHING_PROBABILITY = 0.5
COLLAPSE_PROBABILITY = 0.2
EXPORT_DIR = "drift_exports"
ANIMATION_FRAMES = 10

# Node display labels (ASCII fallback)
LABELS = {
    "origin": "ROOT",
    "normal": "NODE",
    "collapse": "X"
}

# Color map by generation
GEN_COLORS = ["#00ffff", "#00ccff", "#0099ff", "#0066cc", "#003366", "#001f4d", "#000d1a"]

# Ensure export directory exists
os.makedirs(EXPORT_DIR, exist_ok=True)

# === FUNCTIONAL MODULES ===

def generate_drift_graph(generations):
    G = nx.DiGraph()
    node_counter = 0
    node_info = {}  # Stores generation and type

    def recurse(node_name, generation):
        nonlocal node_counter
        if generation >= generations:
            return

        branches = random.randint(1, 3) if random.random() < BRANCHING_PROBABILITY else 0
        for _ in range(branches):
            node_counter += 1
            new_node = f"{node_counter}"
            G.add_edge(node_name, new_node)
            node_info[new_node] = {"gen": generation + 1, "type": "normal"}
            recurse(new_node, generation + 1)

        if random.random() < COLLAPSE_PROBABILITY:
            collapse_node = f"X_{node_name}"
            G.add_edge(node_name, collapse_node)
            node_info[collapse_node] = {"gen": generation + 1, "type": "collapse"}

    root = "origin"
    G.add_node(root)
    node_info[root] = {"gen": 0, "type": "origin"}
    recurse(root, 0)
    return G, node_info


def visualize_graph(G, node_info, filename=None):
    pos = nx.spring_layout(G, iterations=200, seed=42)
    plt.figure(figsize=(14, 10))

    for node in G.nodes():
        gen = node_info[node]["gen"]
        ntype = node_info[node]["type"]
        color = GEN_COLORS[gen] if gen < len(GEN_COLORS) else GEN_COLORS[-1]
        label = LABELS.get(ntype, "?")
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=color, node_size=500)
        nx.draw_networkx_labels(G, pos, labels={node: label}, font_size=8, font_color='black')

    nx.draw_networkx_edges(G, pos, arrows=True)
    plt.title("Recursive Civilization Drift Field (Fractal Evolution)")
    plt.axis('off')

    if filename:
        plt.savefig(os.path.join(EXPORT_DIR, filename), bbox_inches='tight')
    else:
        plt.show()
    plt.close()


def create_animation():
    fig, ax = plt.subplots(figsize=(14, 10))
    pos = None

    def update(frame):
        ax.clear()
        G, node_info = generate_drift_graph(generations=frame + 2)
        nonlocal pos
        pos = nx.spring_layout(G, seed=42) if pos is None else pos
        for node in G.nodes():
            gen = node_info[node]["gen"]
            ntype = node_info[node]["type"]
            color = GEN_COLORS[gen] if gen < len(GEN_COLORS) else GEN_COLORS[-1]
            label = LABELS.get(ntype, "?")
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=color, node_size=500, ax=ax)
            nx.draw_networkx_labels(G, pos, labels={node: label}, font_size=8, font_color='black', ax=ax)
        nx.draw_networkx_edges(G, pos, arrows=True, ax=ax)
        ax.set_title(f"Drift Field Generation {frame + 1}")
        ax.axis('off')

    anim = FuncAnimation(fig, update, frames=ANIMATION_FRAMES, repeat=False)
    anim.save(os.path.join(EXPORT_DIR, "drift_evolution.gif"), writer='pillow')
    plt.close()


# === EXECUTION ===
if __name__ == "__main__":
    G, node_info = generate_drift_graph(GENERATIONS)
    visualize_graph(G, node_info, filename="static_drift_map.png")
    create_animation()
