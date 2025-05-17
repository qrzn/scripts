import random
import datetime
import os
import json

# === CONFIGURATION ===
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

EVENTS = list(GLYPH_MAP.keys())

SAVE_DIR = "drift_logs"
SESSION_FILE_PREFIX = "drift_session_"

def generate_event():
    """Randomly generate a drift event for testing."""
    return random.choice(EVENTS)

def log_drift_session(cycles=20):
    session_log = []
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    filename = os.path.join(SAVE_DIR, f"{SESSION_FILE_PREFIX}{timestamp}.json")

    print("\n[ Drift Logger Activated ]\n")
    for cycle in range(cycles):
        event = generate_event()
        glyph = GLYPH_MAP[event]
        session_log.append({
            "Cycle": cycle + 1,
            "Event": event,
            "Glyph": glyph,
            "Timestamp": datetime.datetime.now().isoformat()
        })
        print(f"Cycle {cycle + 1}: {event} {glyph}")

    # Save session
    with open(filename, "w") as f:
        json.dump(session_log, f, indent=2)

    print(f"\n[ Drift Session Saved: {filename} ]")
    return session_log

def main():
    print("Symbolic Drift Logger\n")
    try:
        cycles = int(input("Enter number of drift cycles to simulate: ").strip())
    except ValueError:
        cycles = 20

    log_drift_session(cycles)

if __name__ == "__main__":
    main()
