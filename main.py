import os
import json
from entities.player import Player
from entities.merchant import Merchant
from logic.game_engine import spawn_enemies
from utils.exceptions import *
from items.weapons import *
from items.potions import *


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
        stage += 1
        if stage > 3:
            clear_screen()
            print(f" --- GAME OVER! ---\n{player.name} has won")
            exit()
        input("\nPress Enter to continue...")


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

                game_loop(player, stage=1)

            elif choice == "2":
                # Здесь будет вызов player, stage = load_game()
                pass

            elif choice == "3":
                clear_screen()
                print(" --- Goodbye! ---")
                exit()

            else:
                raise InvalidChoice("Please select an option from 1 to 3.")

        except InvalidChoice as ice:
            # Красим сообщение об ошибке выбора в красный цвет
            print(f"\n\033[31m --- Invalid Choice! {ice} ---\033[0m")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()