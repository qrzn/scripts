import random
import time

# Simulation parameters
WORLD_SIZE = 100
INITIAL_NODES = 10
MAX_CYCLES = 100
SPAWN_CHANCE_AFTER_COLLAPSE = 0.2

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.x = random.randint(0, WORLD_SIZE)
        self.y = random.randint(0, WORLD_SIZE)
        self.stability = random.uniform(0.5, 1.0)  # 0 = instant collapse, 1 = highly stable
        self.drift_tendency = random.uniform(0.1, 1.0)  # 1 = highly chaotic
        self.collapse_threshold = random.uniform(0.2, 0.8)  # threshold where node will collapse

    def update(self):
        # Drift randomly based on drift tendency
        drift_x = random.uniform(-self.drift_tendency, self.drift_tendency)
        drift_y = random.uniform(-self.drift_tendency, self.drift_tendency)
        self.x = max(0, min(WORLD_SIZE, self.x + drift_x))
        self.y = max(0, min(WORLD_SIZE, self.y + drift_y))
        
        # Stability decays slightly each cycle
        self.stability -= random.uniform(0.001, 0.01)

    def is_collapsed(self):
        return self.stability < self.collapse_threshold

class Simulation:
    def __init__(self):
        self.nodes = []
        self.next_id = 0

    def spawn_node(self):
        node = Node(self.next_id)
        self.nodes.append(node)
        self.next_id += 1

    def run_cycle(self, cycle_number):
        print(f"\n[CYCLE {cycle_number}] Active nodes: {len(self.nodes)}")
        
        surviving_nodes = []
        for node in self.nodes:
            node.update()
            if node.is_collapsed():
                print(f"Node {node.id} collapsed at ({node.x:.2f}, {node.y:.2f}).")
                if random.random() < SPAWN_CHANCE_AFTER_COLLAPSE:
                    print(f"New node spawned from collapse of {node.id}.")
                    self.spawn_node()
            else:
                surviving_nodes.append(node)
        
        self.nodes = surviving_nodes

    def run(self):
        print("Starting Autonomous Collapse-Drift Simulation...")
        for _ in range(INITIAL_NODES):
            self.spawn_node()

        for cycle in range(1, MAX_CYCLES + 1):
            self.run_cycle(cycle)
            time.sleep(0.1)  # Short delay for observation

        print("\nSimulation complete.")

if __name__ == "__main__":
    sim = Simulation()
    sim.run()
