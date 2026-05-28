import os
import json
import random
from entities.player import Player
from entities.merchant import Merchant
from logic import inventory
from logic.game_engine import spawn_enemies
from logic.inventory import *
from utils.exceptions import *
from items.weapons import *
from items.potions import *
from entities.merchant import *

petc = "\nPress Enter to continue..."

# ugly but it was attempt to make the code DRY
go = f"--- GAME OVER ---"


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        if not os.environ.get('TERM'):
            os.environ['TERM'] = 'xterm'
        os.system('clear')


def character_creation():
    clear_screen()
    while True:
        name = input("Please enter your name: ")
        try:
            player = Player(name, level=1)
            return player
        except InvalidNameException as ine:
            print(ine)


def check_inventory_menu(player):
    while True:
        clear_screen()
        print(player.inventory.get_inventory_status(player))

        print("--- OPTIONS ---")
        print("1. Inspect item")
        print("2. Back")

        choice = input("\nYour choice: ")

        if choice == "1":
            if not player.inventory.items:
                print("\nNothing to inspect.")
                input(petc)
                continue
            try:
                potions_list = [item for item in player.inventory.items if getattr(item, 'heal', 0) > 0]
                weapons_list = [item for item in player.inventory.items if getattr(item, 'damage', 0) > 0]
                displayed_items = potions_list + weapons_list

                i = int(input("Enter item number: ")) - 1
                if 0 <= i < len(player.inventory.items):
                    item = displayed_items[i]
                    clear_screen()
                    player.inspect(item)

                    if getattr(item, 'heal', 0) > 0:
                        choice_heal = input("\nUse?[y/n]: ")
                        if choice_heal.lower() == "y":
                            player.use_item(item)
                    input(petc)
                else:
                    print("\nInvalid item number.")
                    input(petc)
            except ValueError:
                print("\nPlease enter a number.")
                input(petc)

        elif choice == "2":
            break


def game_loop(player, stage):
    # Control the stage progression up to the maximum level
    while stage <= 5:
        clear_screen()
        print(f"\n=================================")
        print(f"       --- STAGE {stage} / 5 ---")
        print(f"=================================")
        input("\nPress Enter to face the enemies...")

        # The generator yields enemies one by one
        for enemy in spawn_enemies(stage):
            survived = battle_menu(player, enemy)

            if not survived:
                clear_screen()
                print(go)
                exit()

            print(f"\nEnemy {enemy.name} defeated!")
            player.gold += random.randint(25, 75)
            input(petc)

        if stage >= 5:
            clear_screen()
            print("=================================")
            print(f"{'--- VICTORY! GAME OVER ---':^33}")
            print("=================================")
            print(f"Congratulations! {player.name} has won the game!")
            input(petc)
            break

        # Camp sub-loop for preparation before moving to the next stage
        next_stage_ready = False
        while not next_stage_ready:
            clear_screen()
            print(f"--- CAMP (Prepared for Stage {stage + 1}) ---")
            print(f"Player: {player.name} | Gold: {player.gold} | HP: {player.get_hp()}")
            print("\nChoices:")
            print("1. Next stage")
            print("2. Check inventory")
            print("3. Visit merchant")
            print("4. Save game")
            print("5. Exit")

            move = input("\nYour choice: ")

            if move == "1":
                next_stage_ready = True
            elif move == "2":
                check_inventory_menu(player)
            elif move == "3":
                visit_merchant_menu(player, stage)
                input(petc)
            elif move == "4":
                save_game(player, stage)
            elif move == "5":
                exit()
            else:
                print("\n\033[31mInvalid option. Please choose 1-5.\033[0m")
                input(petc)

        stage += 1


def battle_menu(player, enemy):
    clear_screen()
    print("=================================")
    print(f"   BATTLE: vs {enemy.name}!!   ")
    print("=================================\n")

    enemy.introduce()
    input(petc)

    while player.get_hp() > 0 and enemy.get_hp() > 0:
        clear_screen()

        print(f"--- {enemy.name} (HP: {enemy.get_hp()}) ---")
        print(f"--- {player.name} (HP: {player.get_hp()}) ---\n")
        print("1. Attack")
        print("2. Check inventory")

        choice = input("\nYour choice: ")

        if choice == "1":
            dmg = player.get_total_damage()
            enemy.take_damage(dmg)
            print(f"\nYou hit {enemy.name} for {dmg} damage!")

            if enemy.get_hp() <= 0:
                print(f"You defeated {enemy.name}!")
                gold_drop = enemy.get_level() * 15
                player.gold += gold_drop
                print(f"You found {gold_drop} gold.")
                input(petc)
                clear_screen()
                return True
        elif choice == "2":
            check_inventory_menu(player)
            continue

        else:
            print("\nInvalid choice! You stumbled and missed your turn.")

        # Enemy counter-attacks if still alive
        if enemy.get_hp() > 0:
            enemy_dmg = enemy.get_damage()
            player.take_damage(enemy_dmg)
            print(f"{enemy.name} attacked you for {enemy_dmg} damage!")
            input(petc)

    # Returns True if the player survived the battle
    return player.get_hp() > 0


def load_game():
    clear_screen()
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

        print("\n\033[32m --- Game loaded successfully! ---\033[0m")
        input(petc)
        return player, stage

    except (json.JSONDecodeError, KeyError, Exception):
        raise InvalidChoice("Save file is corrupted! Please start a new game.")


def save_game(player: Player, stage: int):
    clear_screen()
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

    print("\n\033[32m --- Game saved successfully! ---\033[0m")
    input(petc)


def visit_merchant_menu(player, stage):
    merchant = Merchant(stage)

    while True:
        clear_screen()
        print(f"Your Gold: {player.gold}")

        sorted_goods = merchant.show_goods()

        if not sorted_goods:
            print("The merchant has run out of items!")
            break

        print("--- OPTIONS ---")
        print("1. Buy item")
        print("2. Back to camp")

        choice = input("\nYour choice: ")

        if choice == "1":
            try:
                i = int(input("Enter item number to buy: ")) - 1
                if 0 <= i < len(sorted_goods):
                    clear_screen()
                    merchant.buy_item(player, i, sorted_goods)
                    input(petc)
                else:
                    print("\nInvalid item number.")
                    input(petc)
            except ValueError:
                print("\nPlease enter a valid number.")
                input(petc)
            except (NotEnoughMoney, NotEnoughSpace) as game_error:
                print(f"\n{game_error}")
                input(petc)

        elif choice == "2":
            break

def main_menu():
    while True:
        clear_screen()
        print(" --- Welcome! ---")
        print("This project was made by Mykyta Hmyriak(s35153) \n")
        print(" --- OPTIONS: ---\n")

        choice = input("1. New game \n2. Load game \n3. Exit\n\nYour choice: ")

        try:
            if choice == "1":
                player = character_creation()

                clear_screen()
                print(" --- Rules and introduction ---\n")
                print("Between each level you will get multiple choices to help you prepare for a new battle.")
                print("You will be able to buy new gear from a merchant, manage your inventory, and heal.\n")
                input("Press Enter to start the adventure...")
                save_game(player, stage=1)

                game_loop(player, stage=1)

            elif choice == "2":
                player, stage = load_game()
                game_loop(player, stage)

            elif choice == "3":
                clear_screen()
                print(" --- Goodbye! ---")
                exit()

            else:
                raise InvalidChoice("Please select an option from 1 to 3.")

        except InvalidChoice as ice:
            print(f"\n\033[31m --- Invalid Choice! {ice} ---\033[0m")
            input(petc)


if __name__ == "__main__":
    main_menu()