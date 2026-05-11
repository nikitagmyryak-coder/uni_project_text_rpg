from entities.entities import Entity

class Wolf(Entity):
    def __init__(self, name, level, hp, damage):
        super().__init__("Lone wolf","animal", level, hp, damage)