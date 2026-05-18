from exceptions_and_functions.exceptions import *

class Inventory():
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.capacity < len(self.items):
            self.items.append(self.items[self.capacity])
            self.capacity += 1
        else:
            raise NotEnoughSpace("Not enough space, the item was dropped")