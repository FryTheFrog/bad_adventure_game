from src.items import Item, Weapon, Armor, Charm, Consumable, KeyItem


class Inventory:
    def __init__(self, gold: int = 0) -> None:
        self.gold = gold
        self.consumables = []
        self.equipment = []
        self.misc = []

        self.weapon_slot = None
        self.armor_slot = None
        self.charm_slot = None

    def check_item(self, item: Item) -> bool:
        if isinstance(item, (Weapon, Armor, Charm)):
            return item in self.equipment
        elif isinstance(item, Consumable):
            return item in self.consumables
        elif isinstance(item, KeyItem):
            return item in self.misc
        else:
            raise TypeError("Unknown item type")

    def add_item(self, item: Item) -> None:
        if isinstance(item, (Weapon, Armor, Charm)):
            self.equipment.append(item)
        elif isinstance(item, Consumable):
            self.consumables.append(item)
        elif isinstance(item, KeyItem):
            self.misc.append(item)
        else:
            raise TypeError("Unknown item type")

    def remove_item(self, item: Item) -> None:
        if not self.check_item(item):
            raise ValueError("Item not in inventory")
        elif isinstance(item, (Weapon, Armor, Charm)):
            self.equipment.remove(item)
        elif isinstance(item, Consumable):
            self.consumables.remove(item)
        elif isinstance(item, KeyItem):
            self.misc.remove(item)
