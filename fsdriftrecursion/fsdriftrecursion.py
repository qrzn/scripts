import os
import hashlib
import json
import time
from datetime import datetime

SNAPSHOT_FILE = "fast_filesystem_snapshot.json"

def generate_file_hash(path, block_size=65536):
    hasher = hashlib.sha256()
    try:
        with open(path, "rb") as file:
            buf = file.read(block_size)
            while buf:
                hasher.update(buf)
                buf = file.read(block_size)
        return hasher.hexdigest()
    except Exception:
        return None  # If file can't be read, return None

def scan_directory(base_path):
    snapshot = {}
    for dirpath, dirnames, filenames in os.walk(base_path):
        for name in filenames:
            filepath = os.path.join(dirpath, name)
            try:
                stats = os.stat(filepath)
                snapshot[filepath] = {
                    "size": stats.st_size,
                    "modified": stats.st_mtime,
                    "hash": generate_file_hash(filepath)
                }
            except FileNotFoundError:
                continue  # Skip files that disappear mid-scan
    return snapshot

def load_snapshot():
    if os.path.exists(SNAPSHOT_FILE):
        with open(SNAPSHOT_FILE, "r") as f:
            return json.load(f)
    return {}

def save_snapshot(snapshot):
    with open(SNAPSHOT_FILE, "w") as f:
        json.dump(snapshot, f, indent=2)

def detect_drift(old_snapshot, new_snapshot):
    added = set(new_snapshot.keys()) - set(old_snapshot.keys())
    removed = set(old_snapshot.keys()) - set(new_snapshot.keys())
    mutated = []

    for path in set(new_snapshot.keys()) & set(old_snapshot.keys()):
        if new_snapshot[path]["hash"] != old_snapshot[path]["hash"]:
            mutated.append(path)

    return added, removed, mutated

def main(base_path):
    print(f"[{datetime.now()}] Scanning filesystem at {base_path}...\n")

    old_snapshot = load_snapshot()
    new_snapshot = scan_directory(base_path)

    added, removed, mutated = detect_drift(old_snapshot, new_snapshot)

    if added or removed or mutated:
        print(f"Drift detected at {datetime.now()}:")
        if added:
            print(f"  + Added: {len(added)} files")
            for path in added:
                print(f"    + {path}")
        if removed:
            print(f"  - Removed: {len(removed)} files")
            for path in removed:
                print(f"    - {path}")
        if mutated:
            print(f"  * Mutated: {len(mutated)} files")
            for path in mutated:
                print(f"    * {path}")
    else:
        print("No drift detected. System stable.\n")

    save_snapshot(new_snapshot)

if __name__ == "__main__":
    base_directory = input("Enter the base directory to scan: ").strip()
    if not os.path.isdir(base_directory):
        print("Invalid directory.")
    else:
        main(base_directory)
