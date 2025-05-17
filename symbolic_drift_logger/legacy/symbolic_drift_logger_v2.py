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

SAVE_DIR = "drift_logs"
SESSION_FILE_PREFIX = "drift_session_"

def list_events():
    print("\nAvailable Events:")
    for idx, (event, glyph) in enumerate(GLYPH_MAP.items(), 1):
        print(f"{idx}: {event} {glyph}")

def manual_event_selection():
    list_events()
    try:
        choice = int(input("\nSelect event by number: ").strip())
        event = list(GLYPH_MAP.keys())[choice - 1]
        glyph = GLYPH_MAP[event]
        return event, glyph
    except (ValueError, IndexError):
        print("Invalid input. Defaulting to Drift 🌀.")
        return "Drift", GLYPH_MAP["Drift"]

def log_drift_session(cycles=20):
    session_log = []
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    filename = os.path.join(SAVE_DIR, f"{SESSION_FILE_PREFIX}{timestamp}.json")

    print("\n[ Drift Logger Activated - Manual Mode ]\n")
    for cycle in range(cycles):
        print(f"\n--- Cycle {cycle + 1} ---")
        event, glyph = manual_event_selection()
        entry = {
            "Cycle": cycle + 1,
            "Event": event,
            "Glyph": glyph,
            "Timestamp": datetime.datetime.now().isoformat()
        }
        session_log.append(entry)
        print(f"Logged: {event} {glyph}")

    # Save session
    with open(filename, "w") as f:
        json.dump(session_log, f, indent=2)

    print(f"\n[ Drift Session Saved: {filename} ]")
    return session_log

def main():
    print("Symbolic Drift Logger (Manual Input Mode)\n")
    try:
        cycles = int(input("Enter number of drift cycles to log: ").strip())
    except ValueError:
        cycles = 20

    log_drift_session(cycles)

if __name__ == "__main__":
    main()
