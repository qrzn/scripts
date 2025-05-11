import random
import time
import os
import matplotlib.pyplot as plt

# Simulation parameters
WORLD_SIZE = 100
INITIAL_NODES = 10
MAX_CYCLES = 100
SPAWN_CHANCE_AFTER_COLLAPSE = 0.2

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

    def run_cycle(self):
        surviving_nodes = []
        collapsed_nodes = []
        
        for node in self.nodes:
            node.update()
            if node.is_collapsed():
                collapsed_nodes.append(node)
                if random.random() < SPAWN_CHANCE_AFTER_COLLAPSE:
                    self.spawn_node()
            else:
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

    def run(self):
        plt.ion()
        fig = plt.figure(figsize=(8, 8))
        fig.patch.set_facecolor('black')

        print("Starting Autonomous Collapse-Drift Simulation (Visualized)...")
        for _ in range(INITIAL_NODES):
            self.spawn_node()

        for _ in range(MAX_CYCLES):
            self.cycle_number += 1
            self.run_cycle()

        plt.ioff()
        plt.show()
        print("\nSimulation complete.")

if __name__ == "__main__":
    sim = Simulation()
    sim.run()
