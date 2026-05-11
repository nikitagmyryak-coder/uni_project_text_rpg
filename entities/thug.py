from entities.entities import Entity

class Thug(Entity):
    def __init__(self, name, level, hp, damage):
        super().__init__(name, "Human", level, hp, damage)