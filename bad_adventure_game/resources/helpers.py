import os

from resources.quest import Quest
from resources.ui import gen_message_ui

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def back_to_village(player, inp):
    if inp == "q":
        player.travel("village")

def inventory(player, inp):
    if inp == "i":
        inv_inp = None
        while inv_inp != "q":
            clear()
            print(player.gen_inv_ui(), end="")
            inv_inp = input()
            item = player.inventory.item_finder(inv_inp)
            if item:
                player.consume_item(item)
                equip = player.un_equip_item(item)
                if equip == False:
                    clear()
                    print(gen_message_ui(";You can only equip;up to 3 items;"), end="")
                    input()
            if inv_inp == "s":
                clear()
                print(player.gen_stats_ui(), end="")
                input()

def buy(player, seller, inp):
    if inp == "b":
        shop_inp = None
        while shop_inp != "q":
            clear()
            print(seller.gen_buy_ui(player), end="")
            shop_inp = input()
            if seller.item_finder(shop_inp):
                item = seller.sell_item(shop_inp)
                if not player.inventory.buy_item(item):
                    seller.buy_item(item)

def sell(player, buyer, inp):
    if inp == "s":
        shop_inp = None
        while shop_inp != "q":
            clear()
            print(player.gen_sell_ui(), end="")
            shop_inp = input()
            if player.inventory.item_finder(shop_inp):
                item = player.inventory.sell_item(shop_inp)
                if not buyer.buy_item(item):
                    player.invetory.buy_item(item)

def battle(player, enemy):
    while True:
        clear()
        print(player.gen_combat_ui(enemy), end="")
        battle_inp = input()
        inventory(player, battle_inp)
        if battle_inp == "a":
            player.hit(enemy)
        if not enemy.is_alive():
            clear()
            print(gen_message_ui(f";YOU WON;you earned {player.get_quest().bounty} coins;"), end="")
            input()
            player.inventory.add_gold(player.get_quest().bounty)
            player.active_quest = None
            break
        enemy.fight(player)
        if not player.is_alive():
            break
        if battle_inp == "q":
            break

def quests(player):
    quest_inp = None
    if not player.get_quest():
        q = Quest()
    else:
        q = player.get_quest()
    while quest_inp != "q":
        clear()
        print(q.gen_board_ui(), end="")
        quest_inp = input()
        if quest_inp == "r":
            player.active_quest = None
            q = Quest()
        elif quest_inp == "a":
            q.toggle_active()
            player.accept_quest(q)
    if player.get_quest():
        return player.get_quest().enemy

def collect(player):
    event = player.collect()
    clear()
    print(gen_message_ui(event), end="")
    input()
