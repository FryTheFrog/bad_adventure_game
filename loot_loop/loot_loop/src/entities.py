from inventory import Inventory

from widgets import HpBar


class Entity:
    def __init__(self, **kwargs) -> None:
        allowed_attr = {"name", "max_hp", "hp", "max_energy",
                        "energy", "dmg", "armor", "luck"}
        self.name = "entity"
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_energy = 100
        self.energy = self.max_energy
        self.dmg = 10
        self.armor = 10
        self.luck = 10
        if kwargs:
            self.__dict__.update(
                (k, v) for k, v in kwargs.item() if k in allowed_attr
            )
        self.inv = Inventory()
        
        self.hp_bar = HpBar()

    def validate_attr(self) -> None:
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.energy > self.max_energy:
            self.energy = self.max_energy
