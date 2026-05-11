from entities.entities import Entity

class Skeleton(Entity):
    def __init__(self, level):
        hp = 15 + (level * 5)
        damage = 10 + (level * 3)
        super().__init__(None, "skeleton", level, hp, damage)