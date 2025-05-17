import os
import json
from datetime import datetime

SNAPSHOT_FILENAME = "fast_filesystem_snapshot.json"

def create_snapshot(base_path, hash_files=False):
    snapshot = {}
    for dirpath, dirnames, filenames in os.walk(base_path):
        for name in filenames:
            filepath = os.path.join(dirpath, name)
            try:
                stats = os.stat(filepath)
                file_info = {
                    "size": stats.st_size,
                    "modified_time": stats.st_mtime
                }
                # Hashing removed by default
                if hash_files:
                    file_info["hash"] = generate_file_hash(filepath)
                snapshot[filepath] = file_info
            except FileNotFoundError:
                continue
    return snapshot

def generate_file_hash(path, block_size=65536):
    import hashlib
    hasher = hashlib.sha256()
    try:
        with open(path, "rb") as file:
            buf = file.read(block_size)
            while buf:
                hasher.update(buf)
                buf = file.read(block_size)
        return hasher.hexdigest()
    except Exception:
        return None

def save_snapshot(snapshot, filename=SNAPSHOT_FILENAME):
    with open(filename, "w") as f:
        json.dump(snapshot, f, indent=2)
    print(f"Snapshot saved to {filename} at {datetime.now()}")

def main():
    base_directory = input("Enter the base directory to snapshot: ").strip()
    if not os.path.isdir(base_directory):
        print("Invalid directory path.")
        return
    choice = input("Hash files? [y/N]: ").strip().lower()
    hash_files = choice == "y"
    snapshot = create_snapshot(base_directory, hash_files=hash_files)
    save_snapshot(snapshot)

if __name__ == "__main__":
    main()
