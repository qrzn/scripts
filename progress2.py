import time
from tqdm import tqdm

text = "Hello, world!"

with tqdm(total=len(text), ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
    for char in text:
        time.sleep(0.1)  # Simulate some processing time
        pbar.write(char)  # Print the character
        pbar.update(1)  # Increment progress bar

print("Text printing complete!")
