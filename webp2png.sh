#!/bin/bash

# Check if ImageMagick's 'convert' is installed
if ! command -v magick &> /dev/null
then
    echo "Error: ImageMagick 'convert' command not found. Install it first."
    exit 1
fi

# Directory to process (defaults to current directory if none provided)
DIR="${1:-.}"

# Check if the directory exists
if [ ! -d "$DIR" ]; then
  echo "Error: Directory '$DIR' does not exist."
  exit 1
fi

# Loop through all .webp files
for file in "$DIR"/*.webp; do
  # Skip if no webp files found
  [ -e "$file" ] || { echo "No .webp files found in '$DIR'."; exit 0; }

  # Get filename without extension
  filename=$(basename "$file" .webp)

  # Convert to PNG
  magick "$file" "$DIR/${filename}.png"
  echo "Converted: $file -> $DIR/${filename}.png"
done

echo "All done."
