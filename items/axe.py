from items.items import Item


class Axe(Item):
    def __init__(self, level):
        if level == 1:
            damage = 30
            description = "Old axe that was stolen from some old man`s cabin"
        elif level == 2:
            damage = 40
            description = "Nice and not so cheap axe"
        else:
            damage = 50
            description = "Combat axe looted from a fallen soldier"
        super().__init__("Axe", 0, damage, description)