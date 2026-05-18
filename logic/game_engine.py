import random
from entities.enemies import (
    Rat, Snake, Wolf, Thug,
    Ghoul, Skeleton, Zombie, Cultist,
    Mercenary, Bear, ForeignSoldier, Ogre
)


def spawn_enemies(stage):

    if stage == 1:
        pool = [Rat, Snake, Wolf, Thug, Ghoul, Skeleton]
        levels = [1, 2]
        count = random.randint(3, 4)

    elif stage == 2:
        pool = [Zombie, Cultist, Mercenary, Bear]
        levels = [3, 4]
        count = 3

    else:
        pool = [ForeignSoldier, Ogre]
        levels = [5]
        count = random.randint(1, 2)

    for _ in range(count):
        enemy_class = random.choice(pool)
        enemy_level = random.choice(levels)
        yield enemy_class(level=enemy_level)