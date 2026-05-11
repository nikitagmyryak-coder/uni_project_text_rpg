from entities.entities import Entity

class Mercenary(Entity):
    def __init__(self, level):
        hp = 55 + (level * 30)
        damage = 60 + (level * 35)
        super().__init__(None, "mercenary", level, hp, damage)