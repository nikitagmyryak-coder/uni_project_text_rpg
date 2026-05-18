from items.items import Item

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
        else:
            heal = 100
            price = 60
            description = "Elixir"

        super().__init__(f"Healing Potion ({description})", heal, 0, price, f"Restores {heal} HP.")