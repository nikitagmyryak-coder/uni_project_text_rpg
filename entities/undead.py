from entities.entities import Entity

class Ghoul(Entity):
    def __init__(self, level):
        hp = 20 + (level * 10)
        damage = 7 + (level * 4)
        super().__init__(None, "ghoul", level, hp, damage)

class Skeleton(Entity):
    def __init__(self, level):
        hp = 25 + (level * 8)
        damage = 10 + (level * 5)
        super().__init__(None, "skeleton", level, hp, damage)

class Zombie(Entity):
    def __init__(self, level):
        hp = 30 + (level * 15)
        damage = 12 + (level * 6)
        super().__init__(None, "zombie", level, hp, damage)

