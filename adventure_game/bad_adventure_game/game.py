#!/usr/bin/env python3
from resources.helpers import *
from resources.ui import *
from resources.entities import Player
from resources.item import Item
from resources.inventory import Smith
from resources.inventory import Witch


# INSTANTIATE ENTITIES
player = Player(30)
player.inventory.add_item(Item("Health Potion", 15, heal=40))
player.inventory.add_item(Item("RedBull", 10, energy_boost=5))
smith = Smith()
witch = Witch()
monster = None

# START GAME
clear()

print(welcome_ui, end="")
input()
player.travel("village")

while True:
    clear()
    inp = None

    match player.get_location():
        case "village":
            print(village_ui, end="")
            inp = input()
            match inp:
                case "1":
                    player.travel("smith")
                case "2":
                    player.travel("hotel")
                case "3":  # notice board
                    monster = quests(player)
                case "4":
                    player.travel("witch")
                case "5":
                    player.travel("forest")

        case "smith":
            print(smith_ui, end="")
            inp = input()
            back_to_village(player, inp)
            inventory(player, inp)
            buy(player, smith, inp)
            sell(player, smith, inp)

        case "witch":
            print(witch_ui, end="")
            inp = input()
            back_to_village(player, inp)
            inventory(player, inp)
            buy(player, witch, inp)
            sell(player, witch, inp)

        case "hotel":
            print(hotel_ui, end="")
            inp = input()
            back_to_village(player, inp)
            inventory(player, inp)
            if inp == "x":
                clear()
                print(gen_message_ui(
                    "You are about to quit;your game will not be saved;I'm to lazy to implement that;x to confirm"
                ), end="")
                quit_inp = input()
                if quit_inp == "x":
                    break

        case "forest":
            print(forest_ui, end="")
            inp = input()
            back_to_village(player, inp)
            inventory(player, inp)
            if inp == "h":
                if not monster:
                    clear()
                    print(gen_message_ui(
                        ";You have not accepted;a hunting quest yet;"
                    ), end="")
                    input()
                    continue
                elif monster:
                    battle(player, monster)
                    monster = None
            if inp == "c":
                collect(player)
