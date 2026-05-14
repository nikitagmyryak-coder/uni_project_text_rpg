from entities.entities import Entity
from exceptions_and_functions.exceptions import *
from items.items import Item

import random
import re

class Player(Entity):
    # we insert level in the beginning of the game so i can add a cheat later to test staff
    def __init__(self, name, level=1):
        max_hp = 100 + (level * 20)
        base_damage = 5 + (level * 5) # + weapon_damage
        if not re.match("^[A-Za-z]+$", name):
             raise InvalidNameException("Invalid name format. Only Latin letter are allowed (no numbers, special characters, etc.)")


        # just a cheat for fun/testing
        if name.lower() == "anon":
            self.max_hp = 9999
            self.current_hp = 9999
            self._damage = 999

        super().__init__(name, "Player", level, max_hp, base_damage)
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.gold = random.randint(25, 101)
        self.inventory = []
        self.equipped_weapon = None
        self.capacity = 8 + (level * 2)
        self.description = "Despite everything, it's still you."

    def health_restore(self):
        self.current_hp = self.max_hp

    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def inspect(self, item):
        level_info = f" [Lvl: {item.level}]" if hasattr(item, 'level') else ""

        print(f"--- {item.name}{level_info} ---")
        print(f"Description: {item.description}")

        # Дополнительно: показываем статы, если это оружие или зелье
        if item.damage > 0:
            print(f"Damage: {item.damage}")
        if item.heal > 0:
            print(f"Heal: {item.heal}")

    def take_damage(self, damage):
        super().take_damage(damage)
        if self.current_hp <= 0:
            print("Game Over. You died.")
            # add a function to exit/load save file



# todo:
# [x] health_restore()
# [x] heal()
# [] equip()
# [x] inspect()
# [x] gold/money
# [] drop_item()
# [] capacity based on level
# [] base_damage vs total_damage
# [x] take_damage
# [] weapon_damage
# [x] cheat
