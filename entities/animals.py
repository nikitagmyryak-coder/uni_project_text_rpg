from entities.entities import Entity

class Wolf(Entity):
    def __init__(self, level):
        hp = 25 + (level * 12)
        damage = 6 + (level * 4)
        super().__init__(None, "wolf", level, hp, damage)

class Snake(Entity):
    def __init__(self, level):
        hp = 15 + (level * 8)
        damage = 8 + (level * 5)
        super().__init__(None, "snake", level, hp, damage)

class Bear(Entity):
    def __init__(self, level):
        hp = 50 + (level * 20)
        damage = 12 + (level * 7)
        super().__init__(None, "bear", level, hp, damage)

class Rat(Entity):
    def __init__(self, level):
        hp = 10 + (level * 5)
        damage = 3 + (level * 2)
        super().__init__(None, "rat", level, hp, damage)