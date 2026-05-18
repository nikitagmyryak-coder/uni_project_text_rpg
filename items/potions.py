from items.items import Item

# potion will have 2 or 3 levels, weak/cheap and good/strong potions
class HealingPotion(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            heal = 25
            price = 10
            description = "Weak potion"
        elif level == 2:
            heal = 50
            price = 25
            description = "Strong potion"

        super().__init__(f"Healing Potion [{description}, Price: {price}]", heal, 0, price)
