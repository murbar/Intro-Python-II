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
    return Player(name, room['outside'])


def print_location(current_room):
    print(f"\nYour current location is {current_room.name}.")
    print(f"{current_room.description}")


def prompt_direction():
    return input(
        "\nWhich direction do you choose? ['N', 'E', 'S', 'W' or 'Q' to quit] ").lower()


def print_impossible_move(cardinal, room_name):
    print(f"\nCannot move {cardinals_verbose[cardinal]} from {room_name}.")


def print_invalid_choice(choice):
    print(f'\nWhoa now... "{choice}" is not a valid choice.')


def end_game():
    print("\nGoodbye for now!")
    exit()


player = init_player()

while(True):

    print_location(player.current_room)

    choice = prompt_direction()

    if not choice:
        continue

    if choice in cardinal_directions:
        next_room = getattr(player.current_room, f"{choice}_to", None)

        if not next_room:
            print_impossible_move(choice, player.current_room.name)
        else:
            player.current_room = next_room

    elif choice == 'q':
        end_game()

    else:
        print_invalid_choice(choice)


# "?" to show options
