from resources.item import Item
from resources.ui import buy_ui


class Inventory:
    def __init__(self, gold=0) -> None:
        self.contents = []
        self.gold = gold

    def add_gold(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise ValueError("invalid amount")
        self.gold += amount

    def add_item(self, item: object) -> None:
        if not isinstance(item, Item):
            raise TypeError("incorrect item type")
        self.contents.append(item)
        self.contents.sort(key=Item.get_price)

    def item_finder(self, item: str) -> object:
        if isinstance(item, str):
            for i in self.contents:
                if i.get_name().lower().strip() == item.lower().strip():
                    item = i
                    break
        if not isinstance(item, Item):
            return False
        if item not in self.contents:
            return False
        return item

    def remove_item(self, item: object) -> None:
        if self.item_finder(item):
            item = self.item_finder(item)
            self.contents.remove(item)
        else:
            return False

    def un_equip_item(self, item: object) -> tuple:
        item = self.item_finder(item)
        if not item:
            return False
        if isinstance(item, Item):
            if not item.equippable:
                return False
            if item.equipped == False:
                item.equipped = True
                return (item.bonus_dmg, item.bonus_armor, item.bonus_luck)
            elif item.equipped == True:
                item.equipped = False
                return (-item.bonus_dmg, -item.bonus_armor, -item.bonus_luck)
        else:
            raise TypeError("incorrect item type")

    def sell_item(self, item) -> object:
        if self.item_finder(item):
            item = self.item_finder(item)
        if isinstance(item, Item):
            self.remove_item(item)
            self.add_gold(item.get_price())
        else:
            raise TypeError("incorrect item type")
        return item

    def buy_item(self, item) -> object:
        if isinstance(item, Item):
            if self.gold >= item.get_price():
                self.add_gold(- item.get_price())
                self.add_item(item)
            else: return False
        else:
            raise TypeError("incorrect item type")
        return item

    def get_contents(self) -> dict:
        res = dict()
        for i in self.contents:
            i = i.get_name()
            res[i] = res.get(i, 0) + 1
        return res

    def inventory_ui_piece(self) -> str:
        seen = []
        ui_str = ""
        for i in self.contents:
            if i.get_name() in seen:
                continue
            count = str(self.get_contents()[i.get_name()])
            if int(count) > 1:
                seen.append(i.get_name())
            if len(count) < 2:
                count = "0" + count
            elif len(count) > 2:
                count = "99"
            ui_str += f"| {count}x {i.item_ui()}\n"
        return ui_str
    
    def gold_ui_piece(self) -> str:
        ui_str = str(self.gold)
        if len(ui_str) > 6:
            ui_str = "999999"
        ui_str = (6 - len(ui_str)) * " " + ui_str
        return ui_str


class Smith(Inventory):
    def __init__(self) -> None:
        super().__init__(1000000)
        self.restock()

    def restock(self) -> None:
        self.add_item(Item("Steel Sword", 100, bonus_dmg=10))
        self.add_item(Item("Titanium Sword", 350, bonus_dmg=20))
        self.add_item(Item("Beskar Sword", 500, bonus_dmg=40))

        self.add_item(Item("Steel Armor", 120, bonus_armor=10))
        self.add_item(Item("Titanium Armor", 400, bonus_armor=30))
        self.add_item(Item("Beskar Armor", 600, bonus_armor=70))
    
    def gen_buy_ui(self, other) -> str:
        ui_str = buy_ui
        return ui_str.format(other.inventory.gold_ui_piece(), self.inventory_ui_piece())


class Witch(Inventory):
    def __init__(self) -> None:
        super().__init__(1000000)
        self.restock()

    def restock(self) -> None:
        self.add_item(Item("Lunar Amulet", 80, bonus_luck=10))
        self.add_item(Item("Solar Amulet", 120, bonus_luck=30))
        self.add_item(Item("Eclipse Amulet", 250, bonus_luck=50))
        self.add_item(Item("Cosmic Amulet", 500, bonus_luck=70))
        for _ in range(99):
            self.add_item(Item("Health Potion", 15, heal=40))
            self.add_item(Item("RedBull", 5, energy_boost=5))

    def gen_buy_ui(self, other) -> str:
        ui_str = buy_ui
        return ui_str.format(other.inventory.gold_ui_piece(), self.inventory_ui_piece())
