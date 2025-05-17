import json
import os
import matplotlib.pyplot as plt

SAVE_DIR = "drift_logs"

GLYPH_MAP = {
    "Drift": "🌀",
    "Collapse": "✖",
    "Recursion Loop": "➿",
    "Entropy Spike": "⚡",
    "Branch": "🌿",
    "Parasite Web": "🕸",
    "Burnout": "🔥",
    "Stagnation": "❄"
}

COLOR_MAP = {
    "Drift": "cyan",
    "Collapse": "red",
    "Recursion Loop": "blue",
    "Entropy Spike": "orange",
    "Branch": "green",
    "Parasite Web": "magenta",
    "Burnout": "yellow",
    "Stagnation": "grey"
}

def load_session(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def plot_session(session_data, title="Drift Trajectory"):
    cycles = [entry["Cycle"] for entry in session_data]
    events = [entry["Event"] for entry in session_data]

    fig, ax = plt.subplots(figsize=(14, 6))
    colors = [COLOR_MAP.get(event, "white") for event in events]

    ax.scatter(cycles, [1]*len(cycles), c=colors, s=100)

    for i, entry in enumerate(session_data):
        ax.text(cycles[i], 1.05, GLYPH_MAP.get(entry["Event"], "?"), ha='center', fontsize=12)

    ax.set_yticks([])
    ax.set_xlabel("Cycle")
    ax.set_title(title)
    ax.set_facecolor('black')
    ax.grid(True)

    plt.show()

def detect_collapse_spiral(session_data):
    collapse_spike = 0
    spiral_threshold = 3
    window = 5

    for i in range(len(session_data) - window + 1):
        window_events = [entry["Event"] for entry in session_data[i:i+window]]
        collapse_count = sum(1 for event in window_events if event in ["Collapse", "Burnout", "Entropy Spike"])
        if collapse_count >= spiral_threshold:
            return True
    return False

def session_statistics(session_data):
    stats = {event: 0 for event in GLYPH_MAP.keys()}
    for entry in session_data:
        stats[entry["Event"]] += 1
    return stats

def compare_sessions(sessions):
    comparison = {}
    for filename, session_data in sessions.items():
        stats = session_statistics(session_data)
        comparison[filename] = stats
    return comparison

def glyph_map_all_sessions():
    files = [f for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    full_sequence = []

    for file in files:
        session_data = load_session(os.path.join(SAVE_DIR, file))
        for entry in session_data:
            full_sequence.append(GLYPH_MAP.get(entry["Event"], "?"))

    print("\n[ Recursive Glyph Map Across Sessions ]\n")
    print(" ".join(full_sequence))

def main():
    print("=== Systemic Recursion Analysis Suite ===\n")
    
    files = [f for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    if not files:
        print("No drift sessions found.")
        return

    sessions = {}
    print("Available Drift Sessions:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}: {file}")

    selected = input("\nSelect sessions to load (comma-separated numbers, or 'all'): ").strip()

    if selected.lower() == 'all':
        for file in files:
            sessions[file] = load_session(os.path.join(SAVE_DIR, file))
    else:
        indices = [int(x.strip())-1 for x in selected.split(",")]
        for idx in indices:
            file = files[idx]
            sessions[file] = load_session(os.path.join(SAVE_DIR, file))

    while True:
        print("\nAvailable Operations:")
        print("1: Visualize Session Trajectory")
        print("2: Compare Session Statistics")
        print("3: Detect Collapse Spirals")
        print("4: Print Full Glyph Map Across Sessions")
        print("5: Exit")

        command = input("\nSelect operation number: ").strip()

        if command == "1":
            for filename, session_data in sessions.items():
                print(f"\nVisualizing: {filename}")
                plot_session(session_data, title=filename)
        
        elif command == "2":
            comparison = compare_sessions(sessions)
            print("\n[ Session Comparison Statistics ]")
            for filename, stats in comparison.items():
                print(f"\n{filename}:")
                for event, count in stats.items():
                    print(f"  {event}: {count}")
        
        elif command == "3":
            print("\n[ Collapse Spiral Detection ]")
            for filename, session_data in sessions.items():
                result = detect_collapse_spiral(session_data)
                status = "SPIRAL DETECTED" if result else "stable"
                print(f"{filename}: {status}")

        elif command == "4":
            glyph_map_all_sessions()

        elif command == "5":
            print("\nExiting Suite.")
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
