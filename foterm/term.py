import os
import shutil
import subprocess
import time


def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

def display_center(file_path):
    columns = shutil.get_terminal_size().columns
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            print_with_delay(line.center(columns))

def print_file_with_delay(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print_with_delay(line)

def main_menu_func():
    while True:
        clear_screen()
        play_sound('ui_hacking_charscroll.wav')
        display_center('greeterheader.txt')
        print_with_delay('Personal Terminal "Proto-Boy" Manufactured by RobCo \n')
        print_with_delay('___________________________________________________ \n\n')
        play_sound('ui_hacking_charscroll.wav')
        print_with_delay('What would you like to do?\n\n')
        options = [
            "View Journal Entries",
            "Log a Journal Entry",
            "Delete a Journal Entry",
            "Proceed to Desktop\n"
        ]
        choice = select_option(options)
        if choice == 1:
            play_sound('ui_hacking_charenter_01.wav')
            view_entries_func()
        elif choice == 2:
            play_sound('ui_hacking_charenter_01.wav')
            write_entry_func()
        elif choice == 3:
            play_sound('ui_hacking_charenter_01.wav')
            delete_entry_func()
        elif choice == 4:
            play_sound('ui_hacking_charenter_01.wav')
            print('Goodbye!')
            break
        else:
            play_sound('ui_hacking_passbad.wav')


def view_entries_func():
    entry_list = ['Go Back']
    entries_dir = os.path.join(os.getcwd(), 'entries')
    for entry_file in os.listdir(entries_dir):
        if os.path.isfile(os.path.join(entries_dir, entry_file)):
            entry_list.append(entry_file)
    
    clear_screen()
    display_center('greeterheader.txt')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo')
    play_sound('ui_hacking_charscroll.wav')
    print('Which Journal Entry would you like to access?')
    choice = select_option(entry_list)
    if choice == 0:
        play_sound('ui_hacking_charenter_01.wav')
        return
    else:
        play_sound('ui_hacking_charenter_01.wav')
    
    clear_screen()
    display_center('greeterheader.txt')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo')
    play_sound('ui_hacking_charscroll.wav')
    entry_file = os.path.join(entries_dir, entry_list[choice])
    print(f'{entry_list[choice]}:')
    play_sound('ui_hacking_charscroll.wav')
    with open(entry_file, 'r') as file:
        for line in file:
            print(line)
    input("Press enter to continue")
    play_sound('ui_hacking_charenter_01.wav')


def write_entry_func():
    clear_screen()
    display_center('greeterheader.txt')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo')
    play_sound('ui_hacking_charscroll.wav')
    entry_name = input("What would you like to name the entry?")
    play_sound('ui_hacking_charenter_01.wav')
    
    clear_screen()
    display_center('greeterheader.txt')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo')
    play_sound('ui_hacking_charscroll.wav')
    print("Press CTRL+D to finalize entry")
    play_sound('ui_hacking_charscroll.wav')
    print(entry_name + ':')
    print()
    entry_content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        entry_content.append(line)
    
    entry_file = os.path.join(os.getcwd(), 'entries', entry_name)
    with open(entry_file, 'w') as file:
        for line in entry_content:
            file.write(line + '\n')
    clear_screen()
    play_sound('ui_hacking_charenter_01.wav')


def delete_entry_func():
    entry_list = ['Go Back']
    entries_dir = os.path.join(os.getcwd(), 'entries')
    for entry_file in os.listdir(entries_dir):
        if os.path.isfile(os.path.join(entries_dir, entry_file)):
            entry_list.append(entry_file)
    
    clear_screen()
    display_center('greeterheader.txt')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo')
    play_sound('ui_hacking_charscroll.wav')
    print('Which Journal Entry would you like to delete?')
    choice = select_option(entry_list)
    if choice == 0:
        play_sound('ui_hacking_charenter_01.wav')
        return
    else:
        play_sound('ui_hacking_charenter_01.wav')
    
    clear_screen()
    display_center('greeterheader.txt')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo')
    play_sound('ui_hacking_charscroll.wav')
    print(f"Delete {entry_list[choice]}? Type YES to continue")
    play_sound('ui_hacking_charscroll.wav')
    confirm_deletion = input()
    if confirm_deletion.upper() == 'YES':
        entry_file = os.path.join(entries_dir, entry_list[choice])
        os.remove(entry_file)
        play_sound('ui_hacking_charenter_01.wav')
        print("FILE DELETED!")
        play_sound('ui_hacking_passgood.wav')
        input()
        repeat_main_menu_func()
    else:
        print("OPERATION CANCELLED")
        play_sound('ui_hacking_charenter_01.wav')
        play_sound('ui_hacking_passbad.wav')
        input()
        repeat_main_menu_func()


def repeat_main_menu_func():
    clear_screen()
    display_center('greeterheader.txt')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo')
    play_sound('ui_hacking_charscroll.wav')
    print('What would you like to do?')
    options = [
        "View Journal Entries",
        "Log a Journal Entry",
        "Delete a Journal Entry",
        "Proceed to Desktop"
    ]
    choice = select_option(options)
    if choice == 1:
        play_sound('ui_hacking_charenter_01.wav')
        view_entries_func()
    elif choice == 2:
        play_sound('ui_hacking_charenter_01.wav')
        write_entry_func()
    elif choice == 3:
        play_sound('ui_hacking_charenter_01.wav')
        delete_entry_func()
    elif choice == 4:
        play_sound('ui_hacking_charenter_01.wav')
        print('Goodbye!')
        return
    else:
        play_sound('ui_hacking_passbad.wav')


def clear_screen():
    subprocess.call('clear' if os.name == 'posix' else 'cls')


def play_sound(file_name):
    subprocess.run(['play', '-q', file_name])


def select_option(options):
    for index, option in enumerate(options):
        print(f'{index+1}. {option}')
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter a valid number.")


def initialize_boot():
    clear_screen()
    play_sound('ui_hacking_charscroll.wav')
    print_with_delay("Initializing boot...\n")
    time.sleep(0.4)
    play_sound('ui_hacking_charscroll.wav')
    print_with_delay("Loading RobCo Unified OS...\n")
    time.sleep(0.4)
    play_sound('ui_hacking_charscroll.wav')
    print_with_delay("64K RAM detected...\n")
    time.sleep(0.4)
    play_sound('ui_hacking_charscroll.wav')
    print_with_delay("Launching Interface...\n")
    play_sound('ui_hacking_passgood.wav')
    time.sleep(0.4)
    clear_screen()
    print_file_with_delay('robco.txt')
    print("==============================================")

    play_sound('ui_hacking_passgood.wav')
    time.sleep(1)
    main_menu_func()


initialize_boot()

