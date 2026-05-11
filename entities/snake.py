from entities.entities import Entity

class Snake(Entity):
    def __init__(self, level):
        hp = level * 15
        damage = level * 8
        super().__init__("Snake", "snake", level, hp, damage)