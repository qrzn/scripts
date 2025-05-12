import random

# Word mutation pools
ADJECTIVES = ["silent", "fractured", "eternal", "recursive", "empty", "drifting", "obscure"]
NOUNS = ["field", "node", "echo", "collapse", "vector", "drift", "anomaly"]
VERBS = ["fractures", "spirals", "dissolves", "mutates", "echoes", "drifts", "collapses"]
LINKERS = ["into", "beyond", "within", "through", "across"]

def generate_sentence():
    adj1 = random.choice(ADJECTIVES)
    noun1 = random.choice(NOUNS)
    verb = random.choice(VERBS)
    link = random.choice(LINKERS)
    adj2 = random.choice(ADJECTIVES)
    noun2 = random.choice(NOUNS)
    
    sentence = f"The {adj1} {noun1} {verb} {link} the {adj2} {noun2}."
    return sentence

def mutate_sentence(sentence):
    words = sentence.split()
    index_to_mutate = random.randint(0, len(words) - 1)
    
    if "field" in words[index_to_mutate] or "node" in words[index_to_mutate]:
        words[index_to_mutate] = random.choice(NOUNS)
    elif "fractured" in words[index_to_mutate] or "silent" in words[index_to_mutate]:
        words[index_to_mutate] = random.choice(ADJECTIVES)
    elif "spirals" in words[index_to_mutate] or "drifts" in words[index_to_mutate]:
        words[index_to_mutate] = random.choice(VERBS)
    elif "into" in words[index_to_mutate] or "through" in words[index_to_mutate]:
        words[index_to_mutate] = random.choice(LINKERS)
    
    mutated = " ".join(words)
    return mutated

def recursive_mutation(start_sentence, cycles=5):
    sentence = start_sentence
    history = [sentence]
    for _ in range(cycles):
        sentence = mutate_sentence(sentence)
        history.append(sentence)
    return history

def main():
    print("Procedural Sentence Mutation Engine\n")
    initial = generate_sentence()
    print(f"Initial Sentence: {initial}\n")
    
    history = recursive_mutation(initial, cycles=10)
    for idx, s in enumerate(history):
        print(f"Cycle {idx}: {s}")

if __name__ == "__main__":
    main()
