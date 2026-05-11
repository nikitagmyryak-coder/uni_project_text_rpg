class Entity:
    def __init__(self, name, race, level, hp, damage):
        self.name = name
        self.race = race
        self._level = level
        self._hp = hp
        self._damage = damage

    def introduce (self):
        print(f"My name is {self.name} and I am a {self.race}, I have {self._hp} HP and do {self._damage} damage")


    def get_level(self):
        return self._level

    def get_hp(self):
        return self._hp

    def get_damage(self):
        return self._damage

    # add live/death variable later
    def take_damage (self, damage):
        if damage < self._hp:
            self._hp -= damage

