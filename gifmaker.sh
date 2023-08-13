#!/bin/bash

center_text_file() {
    if [[ $# -ne 1 ]]; then
        echo "Usage: center_text_file <filename>"
        return 1
    fi

    local filename="$1"
    local lines=()
    local max_width=0

    # Read file into an array of lines
    while IFS= read -r line; do
        lines+=("$line")
        length=${#line}
        if (( length > max_width )); then
            max_width=$length
        fi
    done < "$filename"

    # Calculate padding for horizontal centering
    terminal_width=$(tput cols)
    padding=$(( (terminal_width - max_width) / 2 ))
  
    # Calculate padding for vertical centering
    terminal_height=$(tput lines)
    lines_to_center=$(( (terminal_height - ${#lines[@]}) / 2 ))

    colors=("31" "32" "33" "34" "35" "36" "37")  # ANSI color codes
    current_color=0

    # Record the terminal session using ttyrec
    ttyrec -o "$HOME/Schreibtisch/recording.ttyrec" &

    end_time=$((SECONDS + 11))  # Record for 11 seconds

    while (( SECONDS < end_time )); do
        clear  # Clear the terminal screen
        # Print empty lines for vertical centering
        for ((i = 0; i < lines_to_center; i++)); do
            echo
        done

        # Display centered lines with changing colors
        for line in "${lines[@]}"; do
            color="${colors[current_color]}"
            printf "\e[${color}m%${padding}s%s\e[0m\n" "" "$line"
        done

        sleep 1  # Wait for a second

        current_color=$(( (current_color + 1) % 7 ))  # Switch between colors
    done

    # Stop recording the terminal session
    killall -q ttyrec
    sleep 1

    # Convert ttyrec recording to GIF using ttygif
    ttygif recording.ttyrec -out output.gif

    # Clean up temporary files
    rm recording.ttyrec
}

# Use the specified file path
file_path="$HOME/git/qrzn.github.io/tools/headers/md.txt"
center_text_file "$file_path"
