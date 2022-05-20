from src.inventory import Inventory
from src.widgets import HpBar, EnergyBar


class Entity:
    def __init__(self, **kwargs) -> None:
        allowed_attr = {
            "name",
            "max_hp",
            "hp",
            "max_energy",
            "energy",
            "dmg",
            "armor",
            "luck",
        }
        self.name = "entity"
        self.max_hp = 100
        self.max_energy = 100
        self.dmg = 10
        self.armor = 10
        self.luck = 10
        if kwargs:
            self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_attr)

        self.hp = self.max_hp
        self.energy = self.max_energy

        self.inv = Inventory()
        self.hp_bar = HpBar(self.name, self.max_hp, self.hp)
        self.en_bar = EnergyBar(self.max_energy, self.energy)

    def update_attr(self) -> None:
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.energy > self.max_energy:
            self.energy = self.max_energy
        if self.hp < 0:
            self.hp = 0
        if self.energy < 0:
            self.energy = 0

        self.hp_bar.cur = self.hp
        self.en_bar.cur = self.energy

    def attack(self, other) -> None:
        other.hp -= 10
        other.update_attr()

    def is_alive(self):
        return self.hp > 0


class Player(Entity):
    pass
