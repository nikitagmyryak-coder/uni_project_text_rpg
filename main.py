import os
import json
from entities.player import Player
from entities.merchant import Merchant
from logic.game_engine import spawn_enemies
from utils.exceptions import *
from items.weapons import *
from items.potions import *

#press enter to continue
petc = "\nPress Enter to continue..."

def clear_screen():
    # Determines the OS and clears the screen for better visual
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


def game_loop(player, stage):
    while True:
        clear_screen()
        print(f"\n--- STAGE {stage} ---")
        spawn_enemies(stage)
        input("\n[TEST] Вы зачистили комнату! Нажмите Enter, чтобы перейти дальше...")
        # input("\n --- Choices: \n1. Check inventory \n2. Visit merchant \n 3. Next stage")
        stage += 1
        if stage > 3:
            clear_screen()
            print(f" --- GAME OVER! ---\n{player.name} has won")
            exit()
        input(petc)

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
        player._hp = data["hp"]  # Восстанавливаем приватное здоровье напрямую

        stage = data["stage"]

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

    save_data = {
        "name": player.name,
        "level": player.get_level(),
        "gold": player.gold,
        "hp": player.get_hp(),
        "stage": stage
    }

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=4, ensure_ascii=False)

    print("\n\033[32m --- Game saved successfully! ---\033[0m")
    input(petc)

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
            # Красим сообщение об ошибке выбора в красный цвет
            print(f"\n\033[31m --- Invalid Choice! {ice} ---\033[0m")
            input(petc)

if __name__ == "__main__":
    main_menu()