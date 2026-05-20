import random
import re
from entities.base_entity import Entity
from items.weapons import Dagger
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
        self.gold = random.randint(50, 101)
        self.description = "Despite everything, it's still you."

        self.capacity = 8 + (level * 2)
        self.inventory = Inventory(self.capacity)
        self.equipped_weapon = Dagger(1)
        self.inventory.add_item(self.equipped_weapon)

        if name.lower() == "anon":
            self.max_hp = 9999
            self._hp = 9999
            self._damage = 999
            self.gold = 9999

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
    def equip(self):
        # create a list with only weapons to iterate later on:
        weapons = [item for item in self.inventory.items if getattr(item, 'damage', 0) > 0]
        if weapons:
            best_weapon = max(weapons, key=lambda w: w.damage)
            self.equipped_weapon = best_weapon
        else:
            print("You don't have any weapons.")


    @log_action
    @stat_change_alert
    def level_up(self):
        self._level += 1
        self.capacity += 2
        self.inventory.capacity = self.capacity
        self.max_hp += 20
        self._hp = self.max_hp
        self._damage += 5

    # todo: do something with this
    # def use_item(self, item):
    #     if item in self.inventory.items:
    #         if item.heal > 0:
    #             self.heal(item.heal)
    #             self.inventory.remove_item(item)
    #             print(f"You have used {item.name}.")
    #
    #         elif getattr(item, 'damage', 0) > 0:
    #             print(f"You cannot use {item.name} as a potion! It's a weapon. Use 'Equip' option instead.")
    #
    #         else:
    #             print(f"The item {item.name} cannot be used right now.")
    #
    #     else:
    #         print(f"You don't have {item.name} in your inventory.")