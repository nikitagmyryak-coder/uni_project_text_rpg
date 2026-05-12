from entities.entities import Entity

class Player(Entity):
    def __init__(self, name, player_class):
        super().__init__(name, "Human", 1, 100, 15)
        self.player_class = player_class
        self.inventory = []
        self.description = "Despite everything, it's still you."

    def level_up(self, value):
        if value > self._level:
            diff = value - self._level
            self._level = value
            self._hp += diff * 20
            self._damage += diff * 10
            print(f"Level Up! Now you are level {value}")