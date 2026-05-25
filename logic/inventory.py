from items import potions, weapons
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
        if not self.items:
            return "Your inventory is empty."
        potions_list = [item for item in self.items if getattr(item, 'heal', 0) > 0]
        weapons_list = [item for item in self.items if getattr(item, 'damage', 0) > 0]


        status =  f"Gold: {player.gold}\n" if player else ""
        status += f"--- INVENTORY ({len(self.items)}/{self.capacity}) ---\n"
        item_number = 1

        if potions_list:
            status += "--- Consumables: ---\n"
            for item in potions_list:
                status += f"{item_number}. {item.name}\n"
                item_number += 1

        if weapons_list:
            status += "--- Gear: ---\n"
            for item in weapons_list:
                is_equipped = ""
                if player and hasattr(player, 'equipped_weapon') and item == player.equipped_weapon:
                    is_equipped = " (Equipped)"
                status += f"{item_number}. {item.name}{is_equipped}\n"
                item_number += 1
        return status