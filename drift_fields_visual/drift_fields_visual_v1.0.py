import matplotlib.pyplot as plt
import networkx as nx
import random

# === CONFIGURATION ===
GENERATIONS = 6
INITIAL_POPULATION = 1
BRANCHING_PROBABILITY = 0.5
COLLAPSE_PROBABILITY = 0.2

# === FUNCTIONAL MODULES ===

def generate_drift_graph():
    G = nx.DiGraph()
    node_counter = 0

    def recurse(node_name, generation):
        nonlocal node_counter
        if generation >= GENERATIONS:
            return

        branches = random.randint(1, 3) if random.random() < BRANCHING_PROBABILITY else 0
        for _ in range(branches):
            node_counter += 1
            new_node = f"{node_counter}" 
            G.add_edge(node_name, new_node)
            recurse(new_node, generation + 1)

        # Collapse scenario
        if random.random() < COLLAPSE_PROBABILITY:
            collapse_node = f"collapse_{node_name}"
            G.add_edge(node_name, collapse_node)

    # Start with initial root node
    root = "origin"
    G.add_node(root)
    recurse(root, 0)
    return G


def visualize_graph(G):
    pos = nx.spring_layout(G, iterations=200, seed=42)
    plt.figure(figsize=(14, 10))
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='cyan')
    nx.draw_networkx_edges(G, pos, arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=8)
    plt.title("Recursive Civilization Drift Field (Fractal Evolution)")
    plt.axis('off')
    plt.show()


# === EXECUTION ===
if __name__ == "__main__":
    G = generate_drift_graph()
    visualize_graph(G)
