import random
import matplotlib.pyplot as plt
import os

# === CONFIGURATION ===
NUM_NODES = 10
NUM_FIELDS = 3
CYCLES = 30
ENTROPY_ESCALATION_INTERVAL = 5
PHASE_TRANSITION_INTERVAL = 5
PARASITE_INFECTION_CHANCE = 0.05
AUTONOMOUS_COLLAPSE_THRESHOLD = 2
SAVE_TRAJECTORY_MAP = True

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
MUTATION_TYPES = ["letter_swap", "concept_swap", "symbol_change", "number_drift"]

PHASE_STATES = ["Normal", "High Entropy", "Stable", "Chaotic Collapse"]

class Node:
    def __init__(self, node_id, field_id):
        self.node_id = node_id
        self.alias = self.generate_alias()
        self.field = field_id
        self.infection_layer = 0

    def generate_alias(self):
        greek = random.choice(GREEK_LETTERS)
        concept = random.choice(CONCEPTS)
        symbol = random.choice(SYMBOLS)
        number = random.randint(0, 999)
        return f"{greek}{symbol}{concept}{symbol}{str(number).zfill(3)}"

    def mutate_alias(self, intensity):
        symbol_candidates = [s for s in SYMBOLS if s in self.alias]
        if not symbol_candidates:
            self.alias = self.generate_alias()
            return
        chosen_symbol = random.choice(symbol_candidates)
        parts = self.alias.split(chosen_symbol)

        if len(parts) < 3:
            self.alias = self.generate_alias()
            return

        greek, concept, number = parts[0], parts[1], parts[2]
        symbol = chosen_symbol

        for _ in range(intensity):
            mutation = random.choice(MUTATION_TYPES)
            if mutation == "letter_swap":
                greek = random.choice(GREEK_LETTERS)
            elif mutation == "concept_swap":
                concept = random.choice(CONCEPTS)
            elif mutation == "symbol_change":
                symbol = random.choice(SYMBOLS)
            elif mutation == "number_drift":
                number = str((int(number) + random.randint(-50, 50)) % 1000).zfill(3)

        self.alias = f"{greek}{symbol}{concept}{symbol}{number}"

    def jump_field(self):
        old_field = self.field
        self.field = random.randint(0, NUM_FIELDS - 1)
        print(f"Node-{self.node_id} drifted from Field-{old_field} to Field-{self.field}.")

    def infect(self, other_node):
        if other_node.infection_layer == 0:
            other_node.infection_layer = self.infection_layer + 1
            print(f"⚡ Node-{self.node_id} infected Node-{other_node.node_id} (Layer {other_node.infection_layer}).")

class Simulation:
    def __init__(self):
        self.nodes = [Node(node_id=i, field_id=random.randint(0, NUM_FIELDS - 1)) for i in range(NUM_NODES)]
        self.global_entropy_level = 0
        self.node_history = {}
        self.field_population = {i: 0 for i in range(NUM_FIELDS)}
        self.field_phases = {i: "Normal" for i in range(NUM_FIELDS)}

    def run_cycle(self, cycle_number):
        print(f"\n=== Cycle {cycle_number} ===")

        self.update_field_population()

        surviving_nodes = []
        for node in self.nodes:
            mutation_intensity = self.calculate_mutation_intensity(node)

            node.mutate_alias(mutation_intensity)

            if random.random() < 0.1:
                node.jump_field()

            if random.random() < PARASITE_INFECTION_CHANCE:
                target = random.choice(self.nodes)
                if target != node:
                    node.infect(target)

            surviving_nodes.append(node)

            if node.node_id not in self.node_history:
                self.node_history[node.node_id] = []
            self.node_history[node.node_id].append(node.field)

            print(f"Node-{node.node_id} [Field-{node.field}] Layer-{node.infection_layer} → Alias: {node.alias}")

        self.nodes = surviving_nodes
        self.detect_collisions()
        self.entropy_escalation(cycle_number)
        self.phase_transition(cycle_number)
        self.collapse_check()

    def update_field_population(self):
        self.field_population = {i: 0 for i in range(NUM_FIELDS)}
        for node in self.nodes:
            self.field_population[node.field] += 1

    def calculate_mutation_intensity(self, node):
        base_intensity = node.field + 1 + self.global_entropy_level + (node.infection_layer * 2)
        phase = self.field_phases.get(node.field, "Normal")

        if phase == "High Entropy":
            base_intensity *= 2
        elif phase == "Stable":
            base_intensity = max(1, base_intensity // 2)
        elif phase == "Chaotic Collapse" and random.random() < 0.2:
            node.jump_field()

        return base_intensity

    def detect_collisions(self):
        fragment_map = {}
        for node in self.nodes:
            symbol_candidates = [s for s in SYMBOLS if s in node.alias]
            if not symbol_candidates:
                continue
            chosen_symbol = random.choice(symbol_candidates)
            parts = node.alias.split(chosen_symbol)
            if len(parts) >= 2:
                fragment = parts[1]
                if fragment in fragment_map:
                    other_node = fragment_map[fragment]
                    print(f"⚡ Collision: Node-{node.node_id} ↔ Node-{other_node.node_id} ({fragment})")
                    node.mutate_alias(intensity=3)
                    other_node.mutate_alias(intensity=3)
                    if random.random() < 0.5:
                        node.jump_field()
                    if random.random() < 0.5:
                        other_node.jump_field()
                else:
                    fragment_map[fragment] = node

    def entropy_escalation(self, cycle_number):
        if cycle_number % ENTROPY_ESCALATION_INTERVAL == 0:
            self.global_entropy_level += 1
            print(f"🌪️ Global entropy escalation: Mutation intensity +1 (Level {self.global_entropy_level})")

    def phase_transition(self, cycle_number):
        if cycle_number % PHASE_TRANSITION_INTERVAL == 0:
            for field in self.field_phases:
                self.field_phases[field] = random.choice(PHASE_STATES)
            print(f"⚡ Field Phase Transitions: {self.field_phases}")

    def collapse_check(self):
        for field_id, count in self.field_population.items():
            if count <= AUTONOMOUS_COLLAPSE_THRESHOLD:
                print(f"☢️ Field-{field_id} collapse triggered (Population {count}). Forcing drift.")
                for node in self.nodes:
                    if node.field == field_id:
                        node.jump_field()
                        node.mutate_alias(intensity=5)

    def plot_drift_trajectories(self):
        fig, ax = plt.subplots(figsize=(14, 7))
        colors = ['white', 'cyan', 'magenta', 'yellow', 'red', 'green', 'blue', 'orange']

        for node_id, fields in self.node_history.items():
            cycles = list(range(len(fields)))
            ax.plot(cycles, fields, label=f"Node-{node_id}", color=random.choice(colors))

        ax.set_xlabel('Cycle')
        ax.set_ylabel('Field')
        ax.set_title('Node Drift Trajectories Over Cycles')
        ax.set_facecolor('black')
        ax.grid(True)
        plt.legend()
        if SAVE_TRAJECTORY_MAP:
            if not os.path.exists("output"):
                os.makedirs("output")
            plt.savefig("output/drift_trajectory_map.png", dpi=300, facecolor='black')
        plt.show()

    def run(self):
        print("Multi-Node Collapse-Driven Recursive Drift Simulation Start.\n")
        for cycle in range(1, CYCLES + 1):
            self.run_cycle(cycle)

        print("\nSimulation complete. Plotting drift trajectories...")
        self.plot_drift_trajectories()

if __name__ == "__main__":
    sim = Simulation()
    sim.run()
