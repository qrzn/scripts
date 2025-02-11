# extract_links.py
import os
from bs4 import BeautifulSoup

# Path to your local HTML file
html_file_path = "/home/jan/Schreibtisch/page.html"  # Update if necessary

# Output file where extracted URLs will be saved
output_file = "extracted_links.txt"

# Read and parse the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract all <img> tags and their src attributes
links = []
for img in soup.find_all("img"):
    src = img.get("src")
    if src:
        links.append(src)

# Write the extracted links to the output file
with open(output_file, "w", encoding="utf-8") as out:
    for link in links:
        out.write(link + "\n")

print(f"Extracted {len(links)} links to {output_file}")
