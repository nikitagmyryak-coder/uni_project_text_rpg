from items.items import Item

class Axe(Item):
    def __init__(self, level):
        if level == 1:
            damage, desc = 15, "Rusty hatchet. Good for wood, okay for skulls."
        elif level == 2:
            damage, desc = 30, "Battle axe. A heavy head on a reinforced handle."
        else:
            damage, desc = 55, "Orcish War-Axe. Terrifyingly large and sharp."
        super().__init__("Axe", 0, damage, desc)

class Dagger(Item):
    def __init__(self, level):
        if level == 1:
            damage, desc = 8, "A sharpened piece of scrap metal."
        elif level == 2:
            damage, desc = 18, "Standard military combat knife."
        else:
            damage, desc = 35, "Shadow-step Stiletto. Used by elite assassins."
        super().__init__("Dagger", 0, damage, desc)

class Sword(Item):
    def __init__(self, level):
        if level == 1:
            damage, desc = 12, "Old militia sword, slightly bent."
        elif level == 2:
            damage, desc = 25, "Iron longsword. Reliable and sharp."
        else:
            damage, desc = 48, "Knight's Claymore. A masterwork of steel."
        super().__init__("Sword", 0, damage, desc)

class Mace(Item):
    def __init__(self, level):
        if level == 1:
            damage, desc = 14, "A heavy club with a few rusted nails."
        elif level == 2:
            damage, desc = 28, "Spiked flail. Hard to master, harder to survive."
        else:
            damage, desc = 52, "Holy Mace. Crushes bones and spirits alike."
        super().__init__("Mace", 0, damage, desc)

class Bayonet(Item):
    def __init__(self, level):
        if level == 1:
            damage, desc = 10, "Detached rifle bayonet. Still pointy."
        elif level == 2:
            damage, desc = 20, "Clean military bayonet. Smells of oil and gunpowder."
        else:
            damage, desc = 40, "Special Forces tactical blade."
        super().__init__("Bayonet", 0, damage, desc)

class Gunpowder(Item):
    def __init__(self, level):
        if level == 1:
            damage, desc = 25, "Simple sidearm."
        elif level == 2:
            damage, desc = 50, "Standart issue."
        else:
            damage, desc = 80, "Clean and highly modified custom made rifle."
        super().__init__("Gun", 0, damage, desc)