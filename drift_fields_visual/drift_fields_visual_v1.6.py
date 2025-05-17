import matplotlib.pyplot as plt
import networkx as nx
import random
import os
import json
from matplotlib.animation import FuncAnimation
import plotly.graph_objs as go
import networkx.readwrite.json_graph as jsongraph

# === CONFIGURATION ===
GENERATIONS = 6
BRANCHING_PROBABILITY = 0.5
COLLAPSE_PROBABILITY = 0.2
EXPORT_DIR = "drift_exports"
ANIMATION_FRAMES = 10
MAX_AGE = 3

LABELS = {"origin": "ROOT", "normal": "NODE", "collapse": "X"}
GEN_COLORS = ["#00ffff", "#00ccff", "#0099ff", "#0066cc", "#003366", "#001f4d", "#000d1a"]

os.makedirs(EXPORT_DIR, exist_ok=True)

# === GENERATION ===
def generate_drift_graph(generations):
    G = nx.DiGraph()
    node_counter = 0
    node_info = {}

    def recurse(node_name, generation):
        nonlocal node_counter
        if generation >= generations:
            return

        branches = random.randint(1, 3) if random.random() < BRANCHING_PROBABILITY else 0
        for _ in range(branches):
            node_counter += 1
            new_node = f"{node_name}_{node_counter}"
            G.add_edge(node_name, new_node)
            node_info[new_node] = {"gen": generation + 1, "type": "normal", "age": 0, "entropy": random.random()}
            recurse(new_node, generation + 1)

        if random.random() < COLLAPSE_PROBABILITY:
            collapse_node = f"collapse_{node_name}_{node_counter}"
            G.add_edge(node_name, collapse_node)
            node_info[collapse_node] = {"gen": generation + 1, "type": "collapse", "age": 0, "entropy": 1.0}

    root = "origin"
    G.add_node(root)
    node_info[root] = {"gen": 0, "type": "origin", "age": 0, "entropy": 0.0}
    recurse(root, 0)
    return G, node_info

# === MEMORY AND EXPORT ===
def prune_old_nodes(G, node_info):
    remove = [n for n, i in node_info.items() if i.get("age", 0) > MAX_AGE]
    G.remove_nodes_from(remove)
    for n in remove:
        node_info.pop(n, None)

def export_node_info(node_info, filename="node_info.json"):
    with open(os.path.join(EXPORT_DIR, filename), "w") as f:
        json.dump(node_info, f, indent=2)

# === VISUALIZATION ===
def visualize_graph(G, node_info, filename=None):
    pos = nx.spring_layout(G, iterations=200, seed=42)
    plt.figure(figsize=(14, 10))
    for node in G.nodes():
        if node not in pos: continue
        data = node_info[node]
        color = GEN_COLORS[data['gen']] if data['gen'] < len(GEN_COLORS) else GEN_COLORS[-1]
        label = f"{LABELS.get(data['type'], '?')} ({data['age']})\nEntropy: {data['entropy']:.2f}"
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=color, node_size=500)
        nx.draw_networkx_labels(G, pos, labels={node: label}, font_size=7, font_color='black')
    nx.draw_networkx_edges(G, pos, arrows=True)
    plt.title("Recursive Civilization Drift Field (Fractal Evolution)")
    plt.axis('off')
    if filename:
        plt.savefig(os.path.join(EXPORT_DIR, filename), bbox_inches='tight')
    else:
        plt.show()
    plt.close()

# === INTERACTIVE WEB RENDERING ===
def export_plotly_interactive(G, node_info):
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y, node_x, node_y, texts = [], [], [], [], []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        d = node_info[node]
        texts.append(f"{node}<br>Gen: {d['gen']}<br>Age: {d['age']}<br>Entropy: {d['entropy']:.2f}")

    fig = go.Figure(
        data=[
            go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color='#888'), mode='lines'),
            go.Scatter(x=node_x, y=node_y, mode='markers+text', marker=dict(size=10, color='blue'), text=texts, hoverinfo='text')
        ],
        layout=go.Layout(
            title='Drift Field (Interactive)',
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40)
        )
    )
    fig.write_html(os.path.join(EXPORT_DIR, "interactive_drift.html"))

# === ANIMATION ===
def create_animation():
    fig, ax = plt.subplots(figsize=(14, 10))
    def update(frame):
        ax.clear()
        G, node_info = generate_drift_graph(generations=frame + 2)
        for i in node_info.values(): i["age"] += frame
        prune_old_nodes(G, node_info)
        pos = nx.spring_layout(G, iterations=100, seed=frame)
        for node in G.nodes():
            if node not in pos: continue
            d = node_info[node]
            color = GEN_COLORS[d['gen']] if d['gen'] < len(GEN_COLORS) else GEN_COLORS[-1]
            label = f"{LABELS.get(d['type'], '?')} ({d['age']})\nEntropy: {d['entropy']:.2f}"
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=color, node_size=500, ax=ax)
            nx.draw_networkx_labels(G, pos, labels={node: label}, font_size=7, font_color='black', ax=ax)
        nx.draw_networkx_edges(G, pos, arrows=True, ax=ax)
        ax.set_title(f"Drift Field Generation {frame + 1}")
        ax.axis('off')
    anim = FuncAnimation(fig, update, frames=ANIMATION_FRAMES, repeat=False)
    anim.save(os.path.join(EXPORT_DIR, "drift_evolution.gif"), writer='pillow')
    plt.close()

# === EXECUTION ===
if __name__ == "__main__":
    G, node_info = generate_drift_graph(GENERATIONS)
    export_node_info(node_info)
    visualize_graph(G, node_info, filename="static_drift_map.png")
    export_plotly_interactive(G, node_info)
    create_animation()
