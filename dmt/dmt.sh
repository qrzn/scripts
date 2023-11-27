#!/bin/bash

# Function to simulate actions
simulate_actions() {
    action_type=$1
    count=$2

    if [ "$action_type" == "click" ]; then
        for ((i = 0; i < count; i++)); do
            xdotool click 1
        done
    elif [ "$action_type" == "key" ]; then
        for ((i = 0; i < count; i++)); do
            xdotool key q
        done
    elif [ "$action_type" == "alternate" ]; then
        for ((i = 0; i < count; i++)); do
            if ((i % 2 == 0)); then
                xdotool key q
            else
                xdotool click 1
            fi
        done
    fi
}

# Function to display help
display_help() {
    zenity --info --title="Help" --text="Daggerfall Macro Tool Help:\n\n- Left-Click: Simulate left mouse clicks.\n- Press-Q: Simulate pressing the 'Q' key.\n- Alternate: Alternate between pressing 'Q' and a left mouse click.\n- Help: Display this help information.\n- Exit: Exit the program.\n\nEnter the number of actions to simulate when prompted."
}

while true; do
    # Main menu using Zenity
    user_choice=$(zenity --list --title="Daggerfall Macro Tool" --text="So thou hast decided to abandon virtue and take the easy path? Shame on Thyself" --column="Choice" --column="Description" \
        "Left-Click" "left click spam for selling many items" \
        "Press-Q" "q for recasting spells for exp" \
        "Alternate" "spell spam for exp, destruction magick version" \
        "Help" "Display Help Information" \
        "Exit" "Exit the Program" \
        --height=500 --width=300 --cancel-label="Return to Virtue" --ok-label="CHEATER")

    # Check for cancellation or exit
    if [ $? -ne 0 ] || [ "$user_choice" == "Exit" ]; then
        break
    fi

    # Determine action based on user choice
    action_type=""
    case $user_choice in
        "Left-Click")
            action_type="click"
            ;;
        "Press-Q")
            action_type="key"
            ;;
        "Alternate")
            action_type="alternate"
            ;;
        "Help")
            display_help
            continue
            ;;
        *)
            continue
            ;;
    esac

    # Ask for the number of actions
    action_count=$(zenity --entry --title="Number of Actions" --text="Enter the number of actions:")
    # Check for cancellation
    if [ $? -ne 0 ]; then
        continue
    fi

    # Check if the input is a number
    if ! [[ $action_count =~ ^[0-9]+$ ]]; then
        zenity --error --text="Please enter a valid number."
        continue
    fi

    # Call the function to simulate actions
    simulate_actions "$action_type" "$action_count"

    zenity --info --title="Completion" --text="$action_count actions have been simulated!"
done
