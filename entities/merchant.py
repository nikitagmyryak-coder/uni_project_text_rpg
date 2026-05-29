import random
from items.weapons import Axe, Dagger, Sword, Mace, Bayonet, Gun
from items.potions import HealingPotion, LevelUpPotion
from utils.exceptions import NotEnoughMoney


class Merchant:
    def __init__(self, stage):
        self.stage = stage

        all_possible_items = [
            Axe(stage), Dagger(stage), Sword(stage),
            Mace(stage), Bayonet(stage), Gun(stage),
            HealingPotion(1), HealingPotion(2), LevelUpPotion(stage)
        ]

        self.goods = [item for item in all_possible_items if item.level <= stage]

        self.goods = random.sample(self.goods, k=min(4, len(self.goods)))
        self.goods.append(HealingPotion(stage))

    def show_goods(self):
        print("\n--- MERCHANT SHOP ---")
        print(f"Welcome, traveler! Here is what I have for Stage {self.stage}:")

        sorted_goods = sorted(self.goods, key=lambda item: item.price)

        # enumerate(..., 1) numbers the items starting at 1 instead of 0
        for index, item in enumerate(sorted_goods, 1):
            # Безопасно проверяем наличие урона, если его нет — выводим лечение
            stat_info = f"Damage: {item.damage}" if getattr(item, 'damage', 0) > 0 else f"Heal: {item.heal}"
            print(f"{index}. {item.name} | {stat_info} | Price: {item.price} gold")
            print(f"   Desc: {item.description}")
        print("=" * 55)

        return sorted_goods

    def buy_item(self, player, choice_index, sorted_goods):
        if choice_index < 0 or choice_index >= len(sorted_goods):
            print("Invalid choice!")
            return

        chosen_item = sorted_goods[choice_index]

        if player.gold < chosen_item.price:
            raise NotEnoughMoney(f"You don't have enough gold! You need {chosen_item.price} to buy {chosen_item.name}")

        if isinstance(chosen_item, LevelUpPotion):
            player.gold -= chosen_item.price
            self.goods.remove(chosen_item)
            player.level_up()  # Повышаем уровень на месте
            print(f"Successfully bought and used {chosen_item.name}!")
            return

        try:
            # Inventory capacity check via add_item()
            player.inventory.add_item(chosen_item)
            player.gold -= chosen_item.price
            self.goods.remove(chosen_item)
            print(f"Successfully bought {chosen_item.name} for {chosen_item.price} gold!")
        except Exception as e:
            print(e)