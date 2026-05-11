class Entity:
    def __init__(self, name, race, hp, damage):
        self.name = name
        self.race = race
        self._hp = hp
        self._damage = damage


    def introduce (self):
        print(f"My name is {self.name} and I am a {self.race}")


    # add live/death variable later
    def take_damage (self, damage):
        if damage < self._hp:
            self._hp -= damage

