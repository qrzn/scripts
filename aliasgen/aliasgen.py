import random

# === ALIAS POOLS ===
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

def generate_alias():
    greek = random.choice(GREEK_LETTERS)
    concept = random.choice(CONCEPTS)
    symbol = random.choice(SYMBOLS)
    number = random.randint(0, 999)
    alias = f"{greek}{symbol}{concept}{symbol}{str(number).zfill(3)}"
    return alias

def mutate_alias(alias, intensity=1):
    parts = alias.split(random.choice(SYMBOLS))
    if len(parts) < 3:
        return generate_alias()  # Reset if mutation breaks structure
    
    greek, concept, number = parts[0], parts[1], parts[2]
    
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

    mutated_alias = f"{greek}{symbol}{concept}{symbol}{number}"
    return mutated_alias

def recursive_mutation_cycle(start_alias, cycles=5):
    alias = start_alias
    history = [alias]
    
    for i in range(1, cycles + 1):
        alias = mutate_alias(alias, intensity=i)
        history.append(alias)
    
    return history

def main():
    print("High-Entropy Recursive Node Alias Generator with Mutation System")
    alias = generate_alias()
    print(f"Initial Alias: {alias}\n")
    
    cycles = input("Number of recursive mutation cycles? (default 5): ").strip()
    try:
        cycles = int(cycles)
    except ValueError:
        cycles = 5

    mutation_history = recursive_mutation_cycle(alias, cycles)
    
    print("\nAlias Drift History:")
    for idx, a in enumerate(mutation_history):
        print(f"  Cycle {idx}: {a}")

if __name__ == "__main__":
    main()
