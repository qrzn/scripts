import random
import time
import os
import json
import matplotlib.pyplot as plt

# === CONFIGURATION ===
WORLD_SIZE = 100
INITIAL_NODES = 10
MAX_CYCLES = 100
SPAWN_CHANCE_AFTER_COLLAPSE = 0.2
SAVE_FILE = "simulation_state.json"
ENTROPY_EVENT_CHANCE = 0.1  # 10% per cycle
# ======================

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.x = random.uniform(0, WORLD_SIZE)
        self.y = random.uniform(0, WORLD_SIZE)
        self.stability = random.uniform(0.5, 1.0)
        self.drift_tendency = random.uniform(0.1, 1.0)
        self.collapse_threshold = random.uniform(0.2, 0.8)

    def update(self):
        drift_x = random.uniform(-self.drift_tendency, self.drift_tendency)
        drift_y = random.uniform(-self.drift_tendency, self.drift_tendency)
        self.x = max(0, min(WORLD_SIZE, self.x + drift_x))
        self.y = max(0, min(WORLD_SIZE, self.y + drift_y))
        self.stability -= random.uniform(0.001, 0.01)

    def adaptive_mutation(self):
        if random.random() < 0.2:
            self.stability = min(1.0, self.stability + random.uniform(0.01, 0.05))
            self.drift_tendency = max(0.05, self.drift_tendency - random.uniform(0.01, 0.05))
        if random.random() < 0.05:
            self.stability = random.uniform(0.5, 1.0)
            self.drift_tendency = random.uniform(0.1, 1.0)
            self.collapse_threshold = random.uniform(0.2, 0.8)

    def is_collapsed(self):
        return self.stability < self.collapse_threshold

class Simulation:
    def __init__(self):
        self.nodes = []
        self.next_id = 0
        self.cycle_number = 0

    def spawn_node(self):
        node = Node(self.next_id)
        self.nodes.append(node)
        self.next_id += 1

    def entropy_injection(self):
        print(f"⚡ Entropy Event Triggered at Cycle {self.cycle_number}!")
        event_type = random.choice(["stability_shock", "drift_blast", "mass_collapse"])
        
        if event_type == "stability_shock":
            for node in self.nodes:
                node.stability -= random.uniform(0.05, 0.2)
        elif event_type == "drift_blast":
            for node in self.nodes:
                node.x = max(0, min(WORLD_SIZE, node.x + random.uniform(-10, 10)))
                node.y = max(0, min(WORLD_SIZE, node.y + random.uniform(-10, 10)))
        elif event_type == "mass_collapse":
            for node in self.nodes:
                node.collapse_threshold += random.uniform(0.1, 0.3)

    def run_cycle(self):
        surviving_nodes = []
        collapsed_nodes = []

        if random.random() < ENTROPY_EVENT_CHANCE:
            self.entropy_injection()

        for node in self.nodes:
            node.update()
            if node.is_collapsed():
                collapsed_nodes.append(node)
                if random.random() < SPAWN_CHANCE_AFTER_COLLAPSE:
                    self.spawn_node()
            else:
                node.adaptive_mutation()
                surviving_nodes.append(node)

        self.nodes = surviving_nodes
        self.plot_nodes(collapsed_nodes)

    def plot_nodes(self, collapsed_nodes):
        plt.clf()
        x_alive = [node.x for node in self.nodes]
        y_alive = [node.y for node in self.nodes]
        
        x_collapsed = [node.x for node in collapsed_nodes]
        y_collapsed = [node.y for node in collapsed_nodes]
        
        plt.scatter(x_alive, y_alive, c='white', edgecolors='black', label='Alive Nodes')
        if collapsed_nodes:
            plt.scatter(x_collapsed, y_collapsed, c='red', label='Collapsed Nodes')
        
        plt.xlim(0, WORLD_SIZE)
        plt.ylim(0, WORLD_SIZE)
        plt.title(f"Cycle {self.cycle_number}")
        plt.legend(loc="upper right")
        plt.gca().set_facecolor('black')
        plt.pause(0.1)

    def save_state(self):
        data = [{
            "id": node.id,
            "x": node.x,
            "y": node.y,
            "stability": node.stability,
            "drift_tendency": node.drift_tendency,
            "collapse_threshold": node.collapse_threshold
        } for node in self.nodes]

        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)
        print(f"Simulation state saved to {SAVE_FILE}.")

    def load_state(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
            for entry in data:
                node = Node(entry["id"])
                node.x = entry["x"]
                node.y = entry["y"]
                node.stability = entry["stability"]
                node.drift_tendency = entry["drift_tendency"]
                node.collapse_threshold = entry["collapse_threshold"]
                self.nodes.append(node)
            self.next_id = max(node.id for node in self.nodes) + 1
            print(f"Loaded {len(self.nodes)} nodes from previous session.")

    def run(self):
        plt.ion()
        fig = plt.figure(figsize=(8, 8))
        fig.patch.set_facecolor('black')

        print("Starting Autonomous Collapse-Drift Simulation (Visualized)...")

        self.load_state()
        if not self.nodes:
            for _ in range(INITIAL_NODES):
                self.spawn_node()

        for _ in range(MAX_CYCLES):
            self.cycle_number += 1
            self.run_cycle()

        self.save_state()

        plt.ioff()
        plt.show()
        print("\nSimulation complete.")

if __name__ == "__main__":
    sim = Simulation()
    sim.run()
