from utils.exceptions import *

class Inventory():
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise NotEnoughSpace("Not enough space, the item was not added. Clean some space")


    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    # def the_most_powerfull_weapon(self):
    #     for item in range(len(self.items)):
    #