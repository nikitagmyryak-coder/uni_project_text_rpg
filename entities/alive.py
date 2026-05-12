from entities.entities import Entity

class Cultist(Entity):
    def __init__(self, level):
        hp = level * 25
        damage = level * 25
        super().__init__(None, "cultist", level, hp, damage)


class ForeignSoldier(Entity):
    def __init__(self, level):
        hp = 85 + (level * 40)
        damage = 90 + (level * 45)
        super().__init__(None, "foreign_soldier", level, hp, damage)


class Mercenary(Entity):
    def __init__(self, level):
        hp = 55 + (level * 30)
        damage = 60 + (level * 35)
        super().__init__(None, "mercenary", level, hp, damage)


class Thug(Entity):
    def __init__(self, level):
        hp = 40 + (level * 10)
        damage = 5 + (level * 2)
        super().__init__(None, "thug", level, hp, damage)


class Ogre(Entity):
    def __init__(self, level):
        hp = level * 40
        damage = level * 10
        super().__init__(None, "ogre", level, hp, damage)


