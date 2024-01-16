#!/bin/bash

# Check if a filename is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi

# Extract filename without extension
filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"

# Output file name
output_file="${filename}_compressed.mp4"

# Run FFmpeg command to compress video
ffmpeg -i "$1" -c:v libx265 -b:v 2M -r 60 "$output_file"

# Check if FFmpeg was successful
if [ $? -eq 0 ]; then
  echo "Compression successful. Output saved as $output_file."
else
  echo "Compression failed."
fi