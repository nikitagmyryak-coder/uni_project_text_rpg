from entities.entities import Entity

class Thug(Entity):
    def __init__(self, level):
        hp = 40 + (level * 10)
        damage = 5 + (level * 2)
        super().__init__(None, "thug", level, hp, damage)