from entities.entities import Entity

class Cultist(Entity):
    def __init__(self, level):
        hp = level * 25
        damage = hp * 25
        super().__init__(None, "cultist", level, hp, damage)