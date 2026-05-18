from items.items import Item

class Axe(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            damage, price, desc = 15, 20, "Rusty hatchet. Good for wood, okay for skulls."
        elif level == 2:
            damage, price, desc = 30, 50, "Battle axe. A heavy head on a reinforced handle."
        else:
            damage, price, desc = 55, 120, "Orcish War-Axe. Terrifyingly large and sharp."
        super().__init__("Axe", 0, damage, price, desc)

class Dagger(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            damage, price, desc = 8, 10, "A sharpened piece of scrap metal."
        elif level == 2:
            damage, price, desc = 18, 30, "Standard military combat knife."
        else:
            damage, price, desc = 35, 80, "Shadow-step Stiletto. Used by elite assassins."
        super().__init__("Dagger", 0, damage, price, desc)

class Sword(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            damage, price, desc = 12, 15, "Old militia sword, slightly bent."
        elif level == 2:
            damage, price, desc = 25, 45, "Iron longsword. Reliable and sharp."
        else:
            damage, price, desc = 48, 105, "Knight's Claymore. A masterwork of steel."
        super().__init__("Sword", 0, damage, price, desc)

class Mace(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            damage, price, desc = 14, 18, "A heavy club with a few rusted nails."
        elif level == 2:
            damage, price, desc = 28, 48, "Spiked flail. Hard to master, harder to survive."
        else:
            damage, price, desc = 52, 115, "Holy Mace. Crushes bones and spirits alike."
        super().__init__("Mace", 0, damage, price, desc)

class Bayonet(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            damage, price, desc = 10, 12, "Detached rifle bayonet. Still pointy."
        elif level == 2:
            damage, price, desc = 20, 35, "Clean military bayonet. Smells of oil and gunpowder."
        else:
            damage, price, desc = 40, 90, "Special Forces tactical blade."
        super().__init__("Bayonet", 0, damage, price, desc)

class Gun(Item):
    def __init__(self, level):
        self.level = level
        if level == 1:
            damage, price, desc = 25, 40, "Simple sidearm."
        elif level == 2:
            damage, price, desc = 50, 90, "Standard issue."
        else:
            damage, price, desc = 80, 200, "Clean and highly modified custom made rifle."
        super().__init__("Gun", 0, damage, price, desc)