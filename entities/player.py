from entities.entities import Entity
import random
import re

class Player(Entity):
    # we insert level in the beginning of the game so i can add a cheat later to test staff
    def __init__(self, name, level=1):
        max_hp = 100 + (level * 20)
        base_damage = 15 + (level * 10) # + weapon_damage
        if re.match("^[A-Za-z]+$", name):
            self.name = name
        # else:
        #     raise InvalidNameException()
        #todo: add cheat

        # if name == "anon":
        #     cheat()

        super().__init__(name, "Player", level, max_hp, base_damage)
        self.max_hp = max_hp
        self.gold = random.randint(25, 101)
        self.inventory = []
        self.equipped_weapon = None
        self.capacity = 8 + (level * 2)
        self.description = "Despite everything, it's still you."

    # todo: redo thi bs
    # def level_up(self, value):
    #     if value > self._level:
    #         self._level = value
    #         print(f"Level Up! Now you are level {value}")

# todo:
# [] health_restore()
# [] heal()
# [] equip()
# [] inspect()
# [] gold/money
# [] drop_item()
# [] capacity based on level
# [] base_damage vs total_damage
# [] take_damage
# [] weapon_damage
# [] cheat