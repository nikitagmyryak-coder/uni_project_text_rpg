import random
import re
from entities.base_entity import Entity
from exceptions_and_functions.exceptions import *
from logic.inventory import Inventory


class Player(Entity):
    def __init__(self, name, level=1):
        # Calculate stats based on level
        max_hp = 100 + (level * 20)
        base_damage = 5 + (level * 5)

        # Validate name using regex
        if not re.match("^[A-Za-z]+$", name):
            raise InvalidNameException("Invalid name format. Only Latin letters are allowed.")

        super().__init__(name, "Player", level, max_hp, base_damage)

        # Identity and status
        self.max_hp = max_hp
        self.gold = random.randint(25, 101)
        self.description = "Despite everything, it's still you."

        # Combat and items
        self.capacity = 8 + (level * 2)
        self.inventory = Inventory(self.capacity)
        self.equipped_weapon = None

        # Testing cheat
        if name.lower() == "anon":
            self.max_hp = 9999
            self._hp = 9999
            self._damage = 999



    def inspect(self, item):
        # Print detailed information about an item
        level_info = f" [Lvl: {item.level}]" if hasattr(item, 'level') else ""

        print(f"--- {item.name}{level_info} ---")
        print(f"Description: {item.description}")

        if getattr(item, 'damage', 0) > 0:
            print(f"Damage: {item.damage}")
        if getattr(item, 'heal', 0) > 0:
            print(f"Heal: {item.heal}")



    def get_total_damage(self):
        # Calculate base damage plus equipped weapon damage
        weapon_bonus = self.equipped_weapon.damage if self.equipped_weapon else 0
        return self._damage + weapon_bonus

    def drop_item(self, item):
        # Remove an item from the inventory and unequip if necessary
        if item in self.inventory.items:
            # If the item is currently equipped, we must unequip it first
            if item == self.equipped_weapon:
                self.equipped_weapon = None
                print(f"You unequipped {item.name} before dropping it.")

            self.inventory.items.remove(item)
            print(f"You dropped {item.name}.")
        else:
            print(f"You don't have {item.name} in your inventory.")

    def equip(self, weapon):
        if getattr(weapon, 'damage', 0) > 0:
            self.equipped_weapon = weapon
            print(f"You successfully equipped {weapon.name}!")

    def level_up(self):
        self._level += 1
        self.capacity = 8 + (self._level * 2) #not really DRY but idc
        self.inventory.capacity = self.capacity

# def use_item(self, item):
#     if item in self.inventory.items:
#         if item.heal > 0:
#             self.heal(item.heal)
#             self.inventory.items.remove(item)
#             print(f"Вы использовали {item.name}.")
#     else:
#         print(f"You don't have {item.name} in your inventory.")
# todo:
# [] health_restore()
# [] heal()
# [x] equip()
# [x] inspect()
# [x] gold/money
# [x] drop_item()
# [] capacity based on level
# [] base_damage vs total_damage
# [] take_damage
# [] weapon_damage
# [x] cheat
# [x] level_up()
