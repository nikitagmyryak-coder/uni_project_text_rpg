from entities.entities import Entity

class Ogr(Entity):
    def __init__(self, name, level, hp, damage):
        super().__init__(name, "Ogr", level, hp, damage)