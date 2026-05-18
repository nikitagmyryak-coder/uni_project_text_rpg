from exceptions_and_functions.exceptions import *

class Inventory():
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise NotEnoughSpace("Not enough space, the item was not added. Clean some space")