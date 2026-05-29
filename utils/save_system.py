import os
import json
from entities.player import Player
from utils.exceptions import InvalidChoice

from items.weapons import Axe, Dagger, Sword, Mace, Bayonet, Gun
from items.potions import HealingPotion, LevelUpPotion

def load_game():
    save_path = "data/save.json"

    if not os.path.exists(save_path):
        raise InvalidChoice("No save file found! Please start a new game.")

    try:
        with open(save_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        player = Player(data["name"], level=data["level"])
        player.gold = data["gold"]
        player._hp = data["hp"]
        stage = data["stage"]

        player.inventory.clear_items()
        player.equipped_weapon = None

        for item_data in data.get("inventory", []):
            class_name = item_data["type"]
            item_level = item_data["level"]

            if class_name in globals():
                item_class = globals()[class_name]
                new_item = item_class(item_level)
                player.inventory.add_item(new_item)

        eq_name = data.get("equipped_weapon")
        if eq_name:
            for item in player.inventory.items:
                if item.__class__.__name__ == eq_name:
                    player.equipped_weapon = item
                    break

        return player, stage

    except (json.JSONDecodeError, KeyError, Exception):
        raise InvalidChoice("Save file is corrupted! Please start a new game.")


def save_game(player: Player, stage: int):
    save_dir = "data"
    save_path = "data/save.json"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    inventory_data = []
    for item in player.inventory.items:
        item_info = {
            "type": item.__class__.__name__,
            "level": getattr(item, 'level', 1)
        }
        inventory_data.append(item_info)

    equipped_weapon = player.equipped_weapon.__class__.__name__ if player.equipped_weapon else None

    save_data = {
        "name": player.name,
        "level": player.get_level(),
        "gold": player.gold,
        "hp": player.get_hp(),
        "stage": stage,
        "equipped_weapon": equipped_weapon,
        "inventory": inventory_data
    }

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=4, ensure_ascii=False)
