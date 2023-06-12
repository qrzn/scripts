import os
import shutil
import sys
import time

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

entrylist = ['Go Back']
rawentry = [f for f in os.listdir(os.path.join(BASE_DIR, 'entries')) if os.path.isfile(os.path.join(BASE_DIR, 'entries', f))]
for i in rawentry:
    entrylist.append(i)

COLUMNS = 12


def display_center(file_path):
    columns = shutil.get_terminal_size().columns
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.center(columns))


greeter = '''
Personal Terminal "Proto-Boy" Manufactured by RobCo
___________________________________________________
'''

def mainmenufunc():
    os.system('clear')
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("What would you like to do?")
    
    menu_options = ["View Journal Entries", "Log a Journal Entry", "Delete a Journal Entry", "Proceed to Desktop"]
    while True:
        choice = input("\n".join("{}: {}".format(i + 1, option) for i, option in enumerate(menu_options)) + "\n")
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            choice = int(choice)
            if choice == 1:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                viewentriesfunc()
            elif choice == 2:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                writeentryfunc()
            elif choice == 3:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                deleteentryfunc()
            elif choice == 4:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                print("Goodbye!")
                sys.exit()
        else:
            os.system('play -q {}/ui_hacking_passbad.wav'.format(BASE_DIR))


def viewentriesfunc():
    os.system('clear')
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("Which Journal Entry would you like to access?")
    
    entry_options = entrylist[:]
    while True:
        entry_choice = input("\n".join("{}: {}".format(i + 1, option) for i, option in enumerate(entry_options)) + "\n")
        if entry_choice.isdigit() and 1 <= int(entry_choice) <= len(entry_options):
            entry_choice = int(entry_choice)
            if entry_choice == 1:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                repeatmainmenufunc()
            else:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                selected_entry = entry_options[entry_choice]
                clear_screen()
                display_center("{}/greeterheader.txt".format(BASE_DIR))
                print(greeter)
                os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
                print("{}:".format(selected_entry))
                os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
                with open("{}/entries/{}".format(BASE_DIR, selected_entry), 'r') as file:
                    print(file.read())
                input("Press enter to continue")
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                repeatmainmenufunc()
        else:
            os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))


def writeentryfunc():
    os.system('clear')
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    entrynameinput = input("What would you like to name the entry?\n")
    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
    os.system('clear')
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("Press CTRL+D to finalize entry")
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("{}:".format(entrynameinput))
    print()
    entry_content = sys.stdin.read()
    with open("{}/entries/{}".format(BASE_DIR, entrynameinput), 'w') as file:
        file.write(entry_content)
    with open("{}/entries/{}".format(BASE_DIR, entrynameinput), 'r') as file:
        print(file.read())
    clear_screen()
    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
    repeatmainmenufunc()


def deleteentryfunc():
    os.system('clear')
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("Which Journal Entry would you like to delete?")
    
    entry_options = entrylist[:]
    while True:
        entry_choice = input("\n".join("{}: {}".format(i + 1, option) for i, option in enumerate(entry_options)) + "\n")
        if entry_choice.isdigit() and 1 <= int(entry_choice) <= len(entry_options):
            entry_choice = int(entry_choice)
            if entry_choice == 1:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                repeatmainmenufunc()
            else:
                os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                selected_entry = entry_options[entry_choice]
                clear_screen()
                display_center("{}/greeterheader.txt".format(BASE_DIR))
                print(greeter)
                os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
                print("Delete {}? Type YES to continue".format(selected_entry))
                os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
                confirmdeletion = input()
                if confirmdeletion.upper() == "YES":
                    os.remove("{}/entries/{}".format(BASE_DIR, selected_entry))
                    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                    print("FILE DELETED!")
                    os.system('play -q {}/ui_hacking_passgood.wav'.format(BASE_DIR))
                    time.sleep(0.1)
                    repeatmainmenufunc()
                else:
                    print("OPERATION CANCELLED")
                    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
                    os.system('play -q {}/ui_hacking_passbad.wav'.format(BASE_DIR))
                    time.sleep(0.2)
                    repeatmainmenufunc()
        else:
            os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))


def repeatmainmenufunc():
    clear_screen()
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("What would you like to do?")
    COLUMNS = 12
    menu_options = ["View Journal Entries", "Log a Journal Entry", "Delete a Journal Entry", "Proceed to Desktop"]
    menu_choice = select_option(menu_options)
    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
    if menu_choice == "View Journal Entries":
        viewentriesfunc()
    elif menu_choice == "Log a Journal Entry":
        writeentryfunc()
    elif menu_choice == "Delete a Journal Entry":
        deleteentryfunc()
    elif menu_choice == "Proceed to Desktop":
        print("Goodbye!")
        sys.exit()
    else:
        os.system('play -q {}/ui_hacking_passbad.wav'.format(BASE_DIR))


def mainmenufunc():
    clear_screen()
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("What would you like to do?")
    COLUMNS = 12
    menu_options = ["View Journal Entries", "Log a Journal Entry", "Delete a Journal Entry", "Proceed to Desktop"]
    menu_choice = select_option(menu_options)
    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
    if menu_choice == "View Journal Entries":
        viewentriesfunc()
    elif menu_choice == "Log a Journal Entry":
        writeentryfunc()
    elif menu_choice == "Delete a Journal Entry":
        deleteentryfunc()
    elif menu_choice == "Proceed to Desktop":
        print("Goodbye!")
        sys.exit()
    else:
        os.system('play -q {}/ui_hacking_passbad.wav'.format(BASE_DIR))


def initialize_boot():
    clear_screen()
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("Initializing boot...")
    time.sleep(0.4)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("Loading RobCo Unified OS...")
    time.sleep(0.4)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("64K RAM detected...")
    time.sleep(0.4)
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("Launching Interface...")
    time.sleep(0.4)
    clear_screen()
    print('''

  _____       _      _____                   
 |  __ \     | |    / ____|                  
 | |__) |___ | |__ | |     ___               
 |  _  // _ \| '_ \| |    / _ \              
 | | \ \ (_) | |_) | |___| (_) |             
 |_|__\_\___/|_.__/ \_____\___/|             
  / ____| |      | |     /\   | |            
 | (___ | |_ __ _| |_   /  \  | |_   _  ___  
  \___ \| __/ _` | \ \ / /\ \ | | | | |/ _ \ 
  ____) | || (_| | |\ V / ____ \| | |_| | (_) |
 |_____/ \__\__,_|_| \_/_/    \_\_|\__, |\___/ 
                                    __/ |      
                                   |___/       
        ''')

    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    print("Welcome to RobCo Unified Operating System")
    time.sleep(0.4)
    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
    print("Initializing Personal Terminal 'Proto-Boy'...")
    time.sleep(0.4)
    clear_screen()
    os.system('play -q {}/ui_hacking_charscroll.wav'.format(BASE_DIR))
    display_center("{}/greeterheader.txt".format(BASE_DIR))
    print(greeter)
    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
    print("What would you like to do?")
    COLUMNS = 12
    menu_options = ["View Journal Entries", "Log a Journal Entry", "Delete a Journal Entry", "Proceed to Desktop"]
    menu_choice = select_option(menu_options)
    os.system('play -q {}/ui_hacking_charenter_01.wav'.format(BASE_DIR))
    if menu_choice == "View Journal Entries":
        viewentriesfunc()
    elif menu_choice == "Log a Journal Entry":
        writeentryfunc()
    elif menu_choice == "Delete a Journal Entry":
        deleteentryfunc()
    elif menu_choice == "Proceed to Desktop":
        print("Goodbye!")
        sys.exit()
    else:
        os.system('play -q {}/ui_hacking_passbad.wav'.format(BASE_DIR))


def select_option(options):
    for index, option in enumerate(options):
        print(f"{index + 1}: {option}")
    choice = input("Enter your choice: ")
    return options[int(choice) - 1]


def clear_screen():
    os.system('clear')


if __name__ == "__main__":
    initialize_boot()

