#!/bin/bash

# Check if pandoc is installed
if ! command -v pandoc &>/dev/null; then
  echo "Error: pandoc is not installed. Please install pandoc and try again."
  exit 1
fi

# Define the fixed template path
TEMPLATE=~/git/scripts/html-templates/thelema_template.html

# Ensure the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input.md> <output.html>"
  exit 1
fi

INPUT="$1"
OUTPUT="$2"

# Check if the template file exists
if [ ! -f "$TEMPLATE" ]; then
  echo "Error: Template file '$TEMPLATE' not found."
  exit 1
fi

# Check if the input markdown file exists
if [ ! -f "$INPUT" ]; then
  echo "Error: Input markdown file '$INPUT' not found."
  exit 1
fi

# Convert the markdown to HTML using the fixed template
pandoc "$INPUT" --template="$TEMPLATE" -o "$OUTPUT"

# Check if pandoc executed successfully
if [ $? -eq 0 ]; then
  echo "Conversion successful: '$INPUT' -> '$OUTPUT'"
else
  echo "Error: Conversion failed."
  exit 1
fi
