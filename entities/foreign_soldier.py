from entities.entities import Entity

class ForeignSoldier(Entity):
    def __init__(self, level):
        hp = 85 + (level * 40)
        damage = 90 + (level * 45)
        super().__init__(None, "foreign_soldier", level, hp, damage)