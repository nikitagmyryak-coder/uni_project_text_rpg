from entities.entities import Entity

# ==================== undead ====================
class Ghoul(Entity):
    def __init__(self, level):
        hp = 20 + (level * 10)
        damage = 7 + (level * 4)
        super().__init__(None, "ghoul", level, hp, damage)

class Skeleton(Entity):
    def __init__(self, level):
        hp = 25 + (level * 8)
        damage = 10 + (level * 5)
        super().__init__(None, "skeleton", level, hp, damage)

class Zombie(Entity):
    def __init__(self, level):
        hp = 30 + (level * 15)
        damage = 12 + (level * 6)
        super().__init__(None, "zombie", level, hp, damage)

# ==================== alive ====================
class Cultist(Entity):
    def __init__(self, level):
        hp = 30 + (level * 10)
        damage = 5 + (level * 5)
        super().__init__(None, "cultist", level, hp, damage)

class ForeignSoldier(Entity):
    def __init__(self, level):
        hp = 50 + (level * 15)
        damage = 15 + (level * 8)
        super().__init__(None, "foreign_soldier", level, hp, damage)

class Mercenary(Entity):
    def __init__(self, level):
        hp = 40 + (level * 12)
        damage = 10 + (level * 7)
        super().__init__(None, "mercenary", level, hp, damage)

class Thug(Entity):
    def __init__(self, level):
        hp = 35 + (level * 8)
        damage = 5 + (level * 4)
        super().__init__(None, "thug", level, hp, damage)

class Ogre(Entity):
    def __init__(self, level):
        hp = 60 + (level * 20)
        damage = 8 + (level * 6)
        super().__init__(None, "ogre", level, hp, damage)

# ==================== animals ====================
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