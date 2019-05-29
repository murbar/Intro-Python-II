from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


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

        continue

    elif choice == 'q':
        end_game()

    else:
        print_invalid_choice(choice)
