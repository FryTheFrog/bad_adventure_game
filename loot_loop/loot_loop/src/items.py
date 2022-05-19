class Item:
    def __init__(self, name: str, value: int = 1) -> None:
        self.name = name
        self.value = value
        self.id = name + str(value)

        self.buy_price = round(self.value*1.1)
        self.sell_price = round(self.value*0.9)

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __str__(self) -> str:
        return self.name + " (" + str(self.value) + ")"

class Weapon(Item):
    def __init__(self, name: str, value: int, dmg: int) -> None:
        super().__init__(name, value)
        self.damage = dmg

class Armor(Item):
    def __init__(self, name: str, value: int, armor: int) -> None:
        super().__init__(name, value)
        self.armor = armor

class Charm(Item):
    def __init__(self, name: str, value: int, luck: int) -> None:
        super().__init__(name, value)
        self.luck = luck
        
class Consumable(Item):
    def __init__(self, name: str, value: int, **kwargs) -> None:
        super().__init__(name, value)
        allowed_attr = {"heal", "boost"}
        self.heal = 0
        self.boost = 0
        if kwargs:
            self.__dict__.update(
                (k, v) for k, v in kwargs.item() if k in allowed_attr
            )

class KeyItem(Item):
    def __init__(self, name: str) -> None:
        super().__init__(name, 0)
