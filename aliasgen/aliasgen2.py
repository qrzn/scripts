import random

# === ALIAS COMPONENTS ===
GREEK_LETTERS = [
    "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta",
    "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho",
    "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"
]

CONCEPTS = [
    "Void", "Drift", "Collapse", "Entropy", "Recursion", "Flux",
    "Anomaly", "Vector", "Null", "Divergence", "Singularity", "Fracture",
    "Gradient", "Field", "Pulse", "Cycle", "Threshold", "Shock"
]

SYMBOLS = ["-", "_", ".", ":", "~"]

# === NODE CLASS ===
class AliasNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.alias = self.generate_alias()
        self.stability = random.uniform(0.5, 1.0)  # Collapses below threshold
        self.mutation_rate = random.uniform(0.1, 0.5)

    def generate_alias(self):
        greek = random.choice(GREEK_LETTERS)
        concept = random.choice(CONCEPTS)
        symbol = random.choice(SYMBOLS)
        number = random.randint(0, 999)
        return f"{greek}{symbol}{concept}{symbol}{str(number).zfill(3)}"

    def mutate_alias(self):
        parts = self.alias.split(random.choice(SYMBOLS))
        if len(parts) < 3:
            self.alias = self.generate_alias()
            return
        
        greek, concept, number = parts[0], parts[1], parts[2]
        if random.random() < self.mutation_rate:
            greek = random.choice(GREEK_LETTERS)
        if random.random() < self.mutation_rate:
            concept = random.choice(CONCEPTS)
        if random.random() < self.mutation_rate:
            number = str((int(number) + random.randint(-100, 100)) % 1000).zfill(3)
        self.alias = f"{greek}{random.choice(SYMBOLS)}{concept}{random.choice(SYMBOLS)}{number}"

    def decay_stability(self):
        self.stability -= random.uniform(0.01, 0.05)

    def is_collapsed(self):
        return self.stability < 0.2

# === SIMULATOR CLASS ===
class AliasNetworkSimulator:
    def __init__(self, initial_nodes=10, cycles=50):
        self.nodes = []
        self.next_id = 0
        self.cycles = cycles
        for _ in range(initial_nodes):
            self.spawn_node()

    def spawn_node(self):
        node = AliasNode(self.next_id)
        self.nodes.append(node)
        self.next_id += 1

    def run(self):
        print("Starting Multi-Node Alias Network Drift Simulation...\n")

        for cycle in range(1, self.cycles + 1):
            print(f"[Cycle {cycle}] Active Nodes: {len(self.nodes)}")
            new_nodes = []
            surviving_nodes = []

            # Drift and decay phase
            for node in self.nodes:
                node.mutate_alias()
                node.decay_stability()

                if node.is_collapsed():
                    print(f"  ✖ Node {node.node_id} ({node.alias}) collapsed.")
                    # 50% chance to spawn drifted successor
                    if random.random() < 0.5:
                        new_node = AliasNode(self.next_id)
                        new_node.alias = node.alias  # Inherit partially drifted alias
                        new_node.mutation_rate = random.uniform(0.1, 0.5)
                        new_node.stability = random.uniform(0.5, 1.0)
                        print(f"    → New Node {new_node.node_id} born from drifted collapse.")
                        new_nodes.append(new_node)
                        self.next_id += 1
                else:
                    surviving_nodes.append(node)

            self.nodes = surviving_nodes + new_nodes

            # Inter-node drift perturbation (field effect)
            if len(self.nodes) >= 2 and random.random() < 0.3:
                self.field_interaction()

            # Print current field snapshot
            for node in self.nodes:
                print(f"    • {node.node_id}: {node.alias} (stability {node.stability:.2f})")

            print()

    def field_interaction(self):
        node_a, node_b = random.sample(self.nodes, 2)
        print(f"  ⚡ Field Interaction: {node_a.alias} ↔ {node_b.alias}")

        # Blend parts of aliases during drift contact
        parts_a = node_a.alias.split(random.choice(SYMBOLS))
        parts_b = node_b.alias.split(random.choice(SYMBOLS))

        if len(parts_a) >= 3 and len(parts_b) >= 3:
            blended_alias = f"{parts_a[0]}{random.choice(SYMBOLS)}{parts_b[1]}{random.choice(SYMBOLS)}{parts_a[2]}"
            node_a.alias = blended_alias
            node_b.alias = blended_alias

# === MAIN EXECUTION ===
if __name__ == "__main__":
    sim = AliasNetworkSimulator(initial_nodes=10, cycles=50)
    sim.run()
