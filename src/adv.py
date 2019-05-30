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
    command = input(
        "\nWhat now? ").lower().split(" ")
    if len(command) == 2:
        return command[0], command[1]

    return command[0], None


def print_impossible_move(cardinal, room_name):
    print(f"\nCannot move {cardinals_verbose[cardinal]} from {room_name}.")


def print_help():
    print(
        "\nAvailable actions:",
        "\n'n', 'e', 's', 'w' to move"
        "\n'i' to list your inventory"
        "\n'look [item]' to inspect an item"
        "\n'get [item]' to add an item to your inventory"
        "\n'drop [item]' to leave an item behind"
        "\n'h' for help"
    )


def print_invalid_action(action):
    print(f'''\nHmm... can't seem to "{action}".''')
    print_help()


def print_no_item():
    print(f'\nYou must specify an item.')
    print_help()


def end_game():
    print("\nGoodbye for now!")
    exit()


player = init_player()

while(True):

    print_location(player.current_room)

    action, target = prompt_action()

    if not action:
        print_help()

    if action in cardinal_directions:
        next_room = getattr(player.current_room, f"{action}_to", None)

        if not next_room:
            print_impossible_move(action, player.current_room.name)
        else:
            player.current_room = next_room

    elif action in ['get', 'drop', 'look']:
        if not target:
            print_no_item()

        item = player.current_room.find_item(target)

        if item:
            if action == 'look':
                item.inspect()

            if action == 'get':
                player.add_inventory_item(item.name)

            if action == 'drop':
                player.remove_inventory_item(item.name)

    elif action == 'i':
        player.print_inventory()

    elif action == 'h':
        print_help()

    elif action == 'q':
        end_game()

    else:
        print_invalid_action(action)
