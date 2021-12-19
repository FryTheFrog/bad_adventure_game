from math import floor, ceil
from random import choice
from resources.entities import Monster
from resources.item import Item
from resources.ui import board_ui

class Quest:
    def __init__(self) -> None:
        self.enemy = Monster()
        self.bounty = self.enemy.bounty()
        self.active = False
    
    def toggle_active(self):
        if self.active:
            self.active = False
        elif not self.active:
            self.active = True
        return self.active
    
    def get_difficulty(self):
        if self.bounty <= 175:
            return "easy"
        if self.bounty <= 203:
            return "medium"
        if self.bounty > 203:
            return "hard"
    
    def gen_board_ui(self):
        enemy = self.enemy.name
        padding_len = 51 - len(enemy)
        enemy = floor(padding_len / 2) * " " + enemy + ceil(padding_len / 2) * " "
        difficulty = self.get_difficulty() + (6 - len(self.get_difficulty())) * " "
        if self.active:
            active = 'ACCEPTED ("a" to undo)'
        if not self.active:
            active = '"a" to ACCEPT  |  "r" to REROLL'
        padding_len = 51 - len(active)
        active = floor(padding_len / 2) * " " + active + ceil(padding_len / 2) * " "
        return board_ui.format(self.bounty, enemy, difficulty, active)
