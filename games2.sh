#!/bin/bash

# Game launcher script

declare -A games
games["Action"]="Game 1"
games["Adventure"]="Game 2"
games["Puzzle"]="Game 3"
games["Exit"]=""

# Function to display the menu
show_menu() {
    clear
    echo "Welcome to Game Launcher!"
    echo "------------------------"
    echo "Please select a category:"
    
    # Display the list of categories
    i=1
    for category in "${!games[@]}"; do
        echo "$i. $category"
        ((i++))
    done
    
    echo "0. Exit"
    echo
    read -p "Enter your choice: " choice
    if [ $choice -eq 0 ]; then
        exit
    elif [ $choice -gt 0 ] && [ $choice -le ${#games[@]} ]; then
        selected_category=${!games[@]}  # Get the selected category
        selected_game=${games[$selected_category]}  # Get the game associated with the category
        launch_game "$selected_game"
    else
        echo "Invalid choice. Please try again."
        read -n 1 -s -r -p "Press any key to continue..."
        show_menu
    fi
}

# Function to launch the selected game
launch_game() {
    clear
    echo "Launching $1..."
    sleep 2
    # Add the actual command to launch the game here
    echo "$1 launched!"
    read -n 1 -s -r -p "Press any key to continue..."
    show_menu
}

# Main program
show_menu

