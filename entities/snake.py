from entities.entities import Entity

class Snake(Entity):
    def __init__(self, name, level, hp, damage):
        super().__init__("Snake","animal", level, hp, damage)