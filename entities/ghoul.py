from entities.entities import Entity

class Ghoul(Entity):
    def __init__(self, level):
        hp = level * 7
        damage = 6 + (level * 2)
        super().__init__(None, "ghoul", level, hp, damage)