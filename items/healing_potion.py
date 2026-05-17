from items.items import Item
from entities.player import *

# potion will have 2 or 3 levels, weak/cheap and good/strong potions
class HealingPotion(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            heal = 25
            description = "Weak potion"
        elif level == 2:
            heal = 50
            description = "Strong potion"
        # else:
        #     self.health_restore()
        #     heal = 6769 #doesnt matter, will restore entire health bar dependent on player level
        #     description = "Will heal you entire body"
        super().__init__(f"Healing Potion [{description}]", heal, 0)
