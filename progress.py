import time
from tqdm import tqdm

total_bytes = 1000000  # Total number of bytes to process

with tqdm(total=total_bytes, unit='B', unit_scale=True, unit_divisor=1024, ncols=80) as pbar:
    # Simulate processing bytes
    for processed_bytes in range(total_bytes):
        time.sleep(0.001)  # Simulate some processing time
        pbar.update(1)  # Increment progress bar

print("Processing complete!")

