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

# Make a new player object that is currently in the 'outside' room.

cardinalsVerbose = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West"
}


def printImposibleMove(cardinal, room_name):
    print(f"\nCannot move {cardinalsVerbose[cardinal]} from {room_name}.\n")


print("Welcome to the game.\n")
name = input("What is your name? ")
print(f"\nHello {name}!\n")
player = Player(name, room['outside'])

# Write a loop that:
while(True):
    # Prints the current room name
    # Prints the current description (the textwrap module might be useful here).
    print(f"Your present location is {player.current_room.name}.\n")
    print(f"{player.current_room.description}\n")
    # Waits for user input and decides what to do.
    choice = input(
        "Which direction do you choose? ['N', 'E', 'S', 'W' or 'Q' to quit] ").lower()

    # If the user enters a cardinal direction, attempt to move to the room there.
    if choice == 'n':
        next_room = player.current_room.n_to

        if not next_room:
            # Print an error message if the movement isn't allowed.
            printImposibleMove(choice, player.current_room.name)
        else:
            player.current_room = next_room

        continue

    # If the user enters "q", quit the game.
    elif choice == 'q':
        print("\nGoodbye for now!")
        exit()
