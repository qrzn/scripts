#!/bin/bash

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Pandoc is not found. Please install it first."
    exit 1
fi

# Get URL input from the user
read -p "Enter the URL: " url

# Use curl to fetch the webpage and pandoc to convert it
curl "$url" | pandoc -f html -t plain -o output.txt

echo "Content has been saved to output.txt!"

