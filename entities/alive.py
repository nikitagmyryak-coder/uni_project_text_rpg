from entities.entities import Entity

class Cultist(Entity):
    def __init__(self, level):
        hp = 30 + (level * 10)
        damage = 5 + (level * 5)
        super().__init__(None, "cultist", level, hp, damage)

class ForeignSoldier(Entity):
    def __init__(self, level):
        hp = 50 + (level * 15)
        damage = 15 + (level * 8)
        super().__init__(None, "foreign_soldier", level, hp, damage)

class Mercenary(Entity):
    def __init__(self, level):
        hp = 40 + (level * 12)
        damage = 10 + (level * 7)
        super().__init__(None, "mercenary", level, hp, damage)

class Thug(Entity):
    def __init__(self, level):
        hp = 35 + (level * 8)
        damage = 5 + (level * 4)
        super().__init__(None, "thug", level, hp, damage)

class Ogre(Entity):
    def __init__(self, level):
        hp = 60 + (level * 20)
        damage = 8 + (level * 6)
        super().__init__(None, "ogre", level, hp, damage)