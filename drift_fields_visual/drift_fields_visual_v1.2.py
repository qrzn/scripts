import matplotlib.pyplot as plt
import networkx as nx
import random

# === CONFIGURATION ===
GENERATIONS = 6
INITIAL_POPULATION = 1
BRANCHING_PROBABILITY = 0.5
COLLAPSE_PROBABILITY = 0.2

# Node display labels (ASCII fallback)
LABELS = {
    "origin": "ROOT",
    "normal": "NODE",
    "collapse": "X"
}

# Color map by generation
GEN_COLORS = ["#00ffff", "#00ccff", "#0099ff", "#0066cc", "#003366", "#001f4d", "#000d1a"]

# === FUNCTIONAL MODULES ===

def generate_drift_graph():
    G = nx.DiGraph()
    node_counter = 0
    node_info = {}  # Stores generation and type

    def recurse(node_name, generation):
        nonlocal node_counter
        if generation >= GENERATIONS:
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


def visualize_graph(G, node_info):
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
    plt.show()


# === EXECUTION ===
if __name__ == "__main__":
    G, node_info = generate_drift_graph()
    visualize_graph(G, node_info)
