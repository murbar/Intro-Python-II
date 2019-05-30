# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def find_item(self, item_name):
        # get the first item with name == item_name or None
        item = next(
            (i for i in self.items if i.name.lower() == item_name), None)

        if not item:
            print(f"No '{item_name}' in this room.")

        return item

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
