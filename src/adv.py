from rooms_data import rooms
from player import Player

cardinals_verbose = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West"
}

cardinal_directions = ['n', 'e', 's', 'w']


def init_player():
    print("Welcome to the game.")
    name = None

    while not name:
        name = input("\nWhat is your name? ")

    print(f"\nHello {name}!")
    return Player(name, rooms['outside'])


def print_location(current_room):
    print(f"\nYour current location is {current_room.name}.")
    print(f"{current_room.description}")
    if current_room.items:
        print(
            f"\nHere you see: {', '.join([i.name for i in current_room.items])}")


def prompt_action():
    return input(
        "\nWhat now? ").lower()


def print_impossible_move(cardinal, room_name):
    print(f"\nCannot move {cardinals_verbose[cardinal]} from {room_name}.")


def print_help():
    print(
        "\nAvailable actions:",
        "\n'n', 'e', 's', 'w' to move"
        "\n'get [item]' to add an item to your inventory"
        "\n'drop [item]' to leave an item behind"
        "\n'h' for help"
    )


def print_invalid_action(action):
    print(f'''\nHmm... can't seem to "{action}".''')
    print_help()


def end_game():
    print("\nGoodbye for now!")
    exit()


player = init_player()

while(True):

    print_location(player.current_room)

    action = prompt_action()

    if not action:
        print_help()

    if action in cardinal_directions:
        next_room = getattr(player.current_room, f"{action}_to", None)

        if not next_room:
            print_impossible_move(action, player.current_room.name)
        else:
            player.current_room = next_room

    elif action == 'h':
        print_help()

    elif action == 'q':
        end_game()

    else:
        print_invalid_action(action)
