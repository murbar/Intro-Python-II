# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def print_inventory(self):
        if not self.inventory:
            print("\nYou are not carrying anything.")
        else:
            print(
                f"\nYou are carrying: {', '.join([i.name for i in self.inventory])}")

    def find_inventory_item(self, item_name):
        # get the first item with name == item_name or None
        return next((i for i in self.inventory if i.name == item_name), None)

    def add_inventory_item(self, item_name):
        item = self.current_room.find_item(item_name)
        if item:
            self.inventory.append(item)
            self.current_room.remove_item(item)
        self.print_inventory()

    def remove_inventory_item(self, item_name):
        item = self.find_inventory_item(item_name)
        if item:
            self.inventory.remove(item)
            self.current_room.add_item(item)
        self.print_inventory()
