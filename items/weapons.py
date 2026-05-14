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

class Dagger(Item):
    def __init__(self, level):
        if level == 1:
            damage = 10
            description = "Weak and rusted dagger"
        elif level == 2:
            damage = 20
            description = "Good and well crafted dagger"
        else:
            damage = 50
            description = "Elite killer-assassin dagger"
        super().__init__("Dagger", 0, damage, description)