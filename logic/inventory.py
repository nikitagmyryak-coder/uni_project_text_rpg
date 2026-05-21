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


    def clear_items(self):
        self.items = []

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_inventory_status(self, player=None):
        gold_info = f"Gold: {player.gold}\n" if player else ""
        if not self.items:
            return "Your inventory is empty."
        print(gold_info)
        status = f"--- INVENTORY ({len(self.items)}/{self.capacity}) ---\n"
        for i, item in enumerate(self.items, 1):
            is_equipped = ""
            if player and hasattr(player, 'equipped_weapon') and item == player.equipped_weapon:
                is_equipped = " (Equipped)"


            status += f"{i}. {item.name}{is_equipped}\n"
        return status