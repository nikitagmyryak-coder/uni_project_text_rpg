from entities.entities import Entity

class Wolf(Entity):
    def __init__(self, level):
        hp = level * 20
        damage = hp * 5
        super().__init__("Zombie", "zombie", level, hp, damage)