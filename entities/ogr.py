from entities.entities import Entity

class Ogr(Entity):
    def __init__(self, level):
        hp = level * 40
        damage = level * 10
        super().__init__(None, "ogre", level, hp, damage)