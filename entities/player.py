import random
import re
from entities.base_entity import Entity
from utils.exceptions import *
from logic.inventory import Inventory
from utils.decorators import log_action, stat_change_alert

class Player(Entity):
    def __init__(self, name, level=1):
        max_hp = 100 + (level * 20)
        base_damage = 5 + (level * 5)

        if not re.match("^[A-Za-z]+$", name):
            raise InvalidNameException("Invalid name format. Only Latin letters are allowed.")

        super().__init__(name, "Player", level, max_hp, base_damage)

        self.max_hp = max_hp
        self.gold = random.randint(25, 101)
        self.description = "Despite everything, it's still you."

        self.capacity = 8 + (level * 2)
        self.inventory = Inventory(self.capacity)
        self.equipped_weapon = None

        if name.lower() == "anon":
            self.max_hp = 9999
            self._hp = 9999
            self._damage = 999

    def inspect(self, item):
        level_info = f" [Lvl: {item.level}]" if hasattr(item, 'level') else ""
        print(f"--- {item.name}{level_info} ---")
        print(f"Description: {item.description}")
        if getattr(item, 'damage', 0) > 0:
            print(f"Damage: {item.damage}")
        if getattr(item, 'heal', 0) > 0:
            print(f"Heal: {item.heal}")

    def get_total_damage(self):
        weapon_bonus = self.equipped_weapon.damage if self.equipped_weapon else 0
        return self._damage + weapon_bonus

    def heal(self, amount):
        self._hp = min(self.max_hp, self._hp + amount)
        print(f"Healed for {amount} HP. Current HP: {self._hp}/{self.max_hp}")

    def drop_item(self, item):
        if item in self.inventory.items:
            if item == self.equipped_weapon:
                self.equipped_weapon = None
                print(f"You unequipped {item.name} before dropping it.")
            self.inventory.remove_item(item)
            print(f"You dropped {item.name}.")
        else:
            print(f"You don't have {item.name} in your inventory.")

    @log_action
    def equip(self, weapon):
        if getattr(weapon, 'damage', 0) > 0:
            self.equipped_weapon = weapon
            print(f"You successfully equipped {weapon.name}!")

    @log_action
    @stat_change_alert
    def level_up(self):
        self._level += 1
        self.capacity += 2
        self.inventory.capacity = self.capacity

    def use_item(self, item):
        if item in self.inventory.items:
            if item.heal > 0:
                self.heal(item.heal)
                self.inventory.remove_item(item)
                print(f"You have used {item.name}.")
        else:
            print(f"You don't have {item.name} in your inventory.")