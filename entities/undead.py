from entities.entities import Entity

class Ghoul(Entity):
    def __init__(self, level):
        hp = level * 7
        damage = 6 + (level * 2)
        super().__init__(None, "ghoul", level, hp, damage)


class Skeleton(Entity):
    def __init__(self, level):
        hp = 15 + (level * 5)
        damage = 10 + (level * 3)
        super().__init__(None, "skeleton", level, hp, damage)


class Wolf(Entity):
    def __init__(self, level):
        hp = level * 20
        damage = hp * 5
        super().__init__("Zombie", "zombie", level, hp, damage)