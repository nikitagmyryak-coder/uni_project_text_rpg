from entities.entities import Entity

class Player(Entity):
    def __init__(self, name, hp, damage, player_class, level=1, race="Human"):
        super().__init__(name, race, level, hp, damage)
        self.player_class = player_class
        self.inventory = []