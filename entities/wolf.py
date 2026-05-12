from entities.entities import Entity

class Wolf(Entity):
    def __init__(self, level):
        hp = 20 + (level * 10)
        damage = 5 + (level * 5)
        super().__init__("Lone wolf", "wolf", level, hp, damage)