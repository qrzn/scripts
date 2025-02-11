import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Path to your local HTML file
html_file_path = "/home/jan/Schreibtisch/page.html"  # Update this path if needed

# --- IMPORTANT ---
# If your HTML file was saved from a website, the relative links in it might be intended
# to be resolved against the original website. Set the correct base URL below.
# For example, if the original page was from "https://goblin-heart.net/sadgrl/webmastery/downloads/tiledbgs",
# then set:
base_url = "https://goblin-heart.net/sadgrl/webmastery/downloads/tiledbgs"
# If your links are already absolute (i.e. start with http:// or https://), then this value is not used.
#
# If you leave base_url as an empty string or don't set it properly, relative URLs will be resolved
# against a file:// URL (i.e. the local file), which won't work with requests.
#
# --- END IMPORTANT ---

# Open and read the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Create a folder to store downloaded files
download_folder = "downloaded_files"
os.makedirs(download_folder, exist_ok=True)

# Process each link in the HTML
for link in soup.find_all("a"):
    file_url = link.get("href")
    
    if not file_url:
        continue  # Skip if there's no href
    
    # Resolve relative links using the base URL if provided
    if file_url.startswith(('http://', 'https://')):
        full_url = file_url
    else:
        full_url = urljoin(base_url, file_url)
    
    print("Resolved URL:", full_url)
    
    # Skip file:// URLs since requests can't handle them
    if full_url.startswith("file://"):
        print("Skipping local file URL:", full_url)
        continue
    
    # Derive a filename from the URL (you may want to improve this if URLs have query strings, etc.)
    file_name = os.path.join(download_folder, full_url.split("/")[-1])
    
    try:
        print(f"Downloading: {full_url}")
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an error for bad responses
        
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {full_url}: {e}")

print("Download complete!")
