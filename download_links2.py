# download_links.py
import os
import requests

# File containing the list of URLs (one per line)
input_file = "extracted_links.txt"

# Folder where downloaded files will be saved
download_folder = "downloaded_files"
os.makedirs(download_folder, exist_ok=True)

# Read the list of URLs
with open(input_file, "r", encoding="utf-8") as file:
    links = [line.strip() for line in file if line.strip()]

# Download each file
for url in links:
    # Determine the file name (this simple method takes the last part of the URL)
    file_name = os.path.join(download_folder, url.split("/")[-1])
    try:
        print(f"Downloading: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

print("Download process complete!")
