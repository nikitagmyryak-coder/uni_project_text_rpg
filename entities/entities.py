import random
from entities.constants import ENEMY_NAMES, ENEMY_DESCRIPTIONS


class Entity:
    def __init__(self, name, race, level, hp, damage):
        self.race = race
        self._level = level
        self._hp = hp
        self._damage = damage

        race_key = race.lower()

        # Set random name if none is provided
        if name is None and race_key in ENEMY_NAMES:
            self.name = random.choice(ENEMY_NAMES[race_key])
        else:
            self.name = name

        # Set description based on race and level
        if race_key in ENEMY_DESCRIPTIONS:
            # Using min to prevent IndexError if level is too high
            desc_index = min(level - 1, len(ENEMY_DESCRIPTIONS[race_key]) - 1)
            self.description = ENEMY_DESCRIPTIONS[race_key][desc_index]
        else:
            self.description = ""

    def introduce(self):
        """Print entity information and description."""
        print(f"--- {self.name} ({self.race}) ---")
        print(f"Level: {self._level} | HP: {self._hp} | Damage: {self._damage}")
        if self.description:
            print(f"Description: {self.description}")

    # Getters
    def get_level(self):
        return self._level

    def get_hp(self):
        return self._hp

    def get_damage(self):
        return self._damage

    def take_damage(self, damage):
        """Reduce HP by damage amount, ensuring it doesn't go below 0."""
        if damage < self._hp:
            self._hp -= damage
        else:
            self._hp = 0