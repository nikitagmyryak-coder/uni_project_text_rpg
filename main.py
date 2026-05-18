import os
import json
from entities.player import Player
from entities.merchant import Merchant
from logic.game_engine import spawn_enemies
from utils.exceptions import InvalidNameException, NotEnoughSpace, NotEnoughMoney
from items.weapons import Axe, Dagger, Sword, Mace, Bayonet, Gun
from items.potions import HealingPotion




if __name__ == "__main__":
    main_menu()