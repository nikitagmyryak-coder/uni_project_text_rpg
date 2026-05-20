import os
import json
from entities.player import Player
from entities.merchant import Merchant
from logic.game_engine import spawn_enemies
from utils.exceptions import InvalidNameException, NotEnoughSpace, NotEnoughMoney
from items.weapons import Axe, Dagger, Sword, Mace, Bayonet, Gun
from items.potions import HealingPotion

def character_creation():
    while True:
            name = input("Please enter your name: ")
            try:
                player = Player(name, level=1)
                return player
            except InvalidNameException as ine:
                print(ine)


def main_menu():
    print(" --- Welcome! ---")
    print("This project was made by Mykyta Hmyriak(s35153) \n")
    print(" --- OPTIONS: ---\n")

    while True:
        choice = input("1. New game \n2. Load game \n3. Exit\n")
        if choice == "1":
            player = character_creation()
            stage = 1
            # game_loop(player, stage)
        elif choice == "2":
            # load()
        elif choice == "3":
            print(" --- Goodbye! ---")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()