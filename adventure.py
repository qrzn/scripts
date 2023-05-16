def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious room with two doors.")
    print("Do you go through door 1 or door 2?")
    door_choice = input("> ")

    if door_choice == "1":
        room_1()
    elif door_choice == "2":
        room_2()
    else:
        print("Invalid choice. Try again.")
        start_game()


def room_1():
    print("You enter a room filled with treasures.")
    print("What do you do?")
    print("1. Take the treasures.")
    print("2. Leave the treasures and explore further.")

    action_choice = input("> ")

    if action_choice == "1":
        print("Congratulations! You have won the game!")
    elif action_choice == "2":
        print("You continue exploring and find yourself in another room.")
        room_2()
    else:
        print("Invalid choice. Try again.")
        room_1()


def room_2():
    print("You enter a dark room with a locked chest.")
    print("What do you do?")
    print("1. Try to pick the lock.")
    print("2. Look for a key elsewhere.")

    action_choice = input("> ")

    if action_choice == "1":
        print("You fail to pick the lock. Game over!")
    elif action_choice == "2":
        print("You find a hidden key in the room.")
        print("You unlock the chest and discover more treasures. Congratulations!")
    else:
        print("Invalid choice. Try again.")
        room_2()


start_game()

