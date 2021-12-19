from abc import ABC
from random import randint, choice
from math import floor, ceil

from resources.inventory import Inventory
from resources.inventory import Item
from resources.ui import inventory_ui
from resources.ui import sell_ui
from resources.ui import combat_ui
from resources.ui import stats_ui


class Base(ABC):
    def __init__(self, start_gold=40, **kwargs) -> None:
        self.max_hp = 100
        self.hp = 100
        self.max_energy = 10
        self.energy = 10
        self.dmg = 10
        self.armor = 10
        self.luck = 10
        allowed_attr = {"max_hp", "hp", "energy", "dmg", "armor", "luck"}
        if kwargs:
            self.__dict__.update((k, v) for k, v in kwargs.item() if k in allowed_attr)
        self.inventory = Inventory(start_gold)
        
    def get_max_hp(self):
        return self.max_hp

    def get_hp(self):
        return self.hp
    
    def get_max_energy(self):
        return self.max_energy

    def get_energy(self):
        return self.energy

    def get_flat_dmg(self):
        return self.dmg

    def get_true_dmg(self):
        if randint(0, 100) <= self.luck:
            return self.dmg * 2
        else:
            return self.dmg

    def get_armor(self):
        return self.armor

    def get_luck(self):
        return self.luck

    def is_alive(self) -> bool:
        if self.get_hp() <= 0 or self.energy <= 0:
            return False
        return True

    def consume_item(self, item: object) -> None:
        item = self.inventory.item_finder(item)
        if not item:
            return False
        if isinstance(item, Item):
            if not item.consumable:
                return False
            self.inventory.remove_item(item)
            self.hp += item.heal
            self.energy += item.energy_boost
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            if self.energy > self.max_energy:
                self.energy = self.max_energy
        else:
            raise TypeError("incorrect item type")

    def hit(self, other):
        if isinstance(other, (Player, Monster)):
            self.energy -= 1
            factor = 1 - other.get_armor() // 100
            other.hp -= self.get_true_dmg() * factor
        else:
            raise TypeError("wrong type for 'other'")

    def stats_ui_piece(self):
        ui_str = f"| Health | {self.hp_ui_piece()} |  Energy | {self.energy_ui_piece()} |"
        return ui_str
    
    def det_stats_ui_piece(self):
        return f"""|   Max HP: {self.get_max_hp()}
|   Damage: {self.get_flat_dmg()}
|   Armor: {self.get_armor()}
|   Luck: {self.get_luck()}"""

    def hp_ui_piece(self):  # len of str 23
        ui_str = ceil(23 / self.max_hp * self.get_hp()) * "█"
        ui_str += (23 - len(ui_str)) * " "
        return ui_str

    def energy_ui_piece(self):
        ui_str = ceil(23 / self.max_energy * self.get_energy()) * "█"
        if isinstance(self, Player):
            ui_str += (23 - len(ui_str)) * " "
        elif isinstance(self, Monster):
            ui_str = (23 - len(ui_str)) * " " + ui_str
        return ui_str


class Player(Base):
    def __init__(self, start_gold=40, **kwargs) -> None:
        super().__init__(start_gold, **kwargs)
        self.location = "welcome"
        self.active_quest = None
        self.equipped_items = []

    def get_location(self) -> str:
        return self.location
    
    def get_quest(self) -> object:
        return self.active_quest

    def travel(self, location: str) -> None:
        allowed = {"village", "smith", "witch", "hotel", "forest"}
        if location not in allowed:
            raise ValueError("location does not exist")
        self.location = location

    def un_equip_item(self, item: object) -> None:
        bonus = self.inventory.un_equip_item(item)
        if bonus:
            if sum(bonus) > 0:
                if len(self.equipped_items) >= 3:
                    self.inventory.un_equip_item(item)
                    return False
                self.equipped_items.append(item)
            else:
                self.equipped_items.remove(item)
            self.dmg += bonus[0]
            self.armor += bonus[1]
            self.luck += bonus[2]
    
    def accept_quest(self, quest:object) -> None:
        if quest == self.active_quest:
            self.active_quest = None
        else:
            self.active_quest = quest

    def gen_combat_ui(self, other):
        if isinstance(other, Monster):
            ui_str = combat_ui
            return ui_str.format(other.name_ui_piece(), self.energy_ui_piece(), self.hp_ui_piece(), other.hp_ui_piece())
        else:
            raise TypeError("wrong type for 'other'")

    def collect(self) -> str:
        if self.energy < 2:
            return ";You don't have enough energy;to go on adventures;"
        self.energy -= 1
        event = choice(["find", "trap", "ambush"])
        match event:
            case "find":
                item = choice([Item("Health Potion", 15, heal=40), Item("RedBull", 5, energy_boost=5)])
                self.inventory.add_item(item)
                return f";You found an item:;{item.get_name()};"
            case "trap":
                trap = choice(["snake", "bear trap", "shrooms"])
                match trap:
                    case "snake":
                        self.hp = 1
                        return ";You were bitten by a snek;you almost died!;"
                    case "bear trap":
                        self.hp = 1
                        return ";You stepped into a bear trap;you almost died!;"
                    case "shrooms":
                        self.energy = 1
                        return "You found some shrooms;now you're high as fuck;;and exhausted"
            case "ambush":
                enemy = choice(["wolves", "bear", "bees"])
                match enemy:
                    case "wolves":
                        return "You were ambushed;by a pack of wolves;;you fought them off with ease"
                    case "bear":
                        return "You were ambushed;by a bear;but they suck at being sneaky;you stabbed him"
                    case "bees":
                        self.inventory.add_item(Item("Honey", 50, heal=20))
                        return "You got stung;by a bunch of bees;but then they gave you;some honey to apologise"

    def gen_inv_ui(self):
        ui_str = inventory_ui
        return ui_str.format(self.inventory.gold_ui_piece(), self.stats_ui_piece(), self.inventory.inventory_ui_piece())
    
    def gen_stats_ui(self):
        ui_str = stats_ui
        return ui_str.format(self.inventory.gold_ui_piece(), self.stats_ui_piece(), self.det_stats_ui_piece())

    def gen_sell_ui(self):
        ui_str = sell_ui
        return ui_str.format(self.inventory.gold_ui_piece(), self.inventory.inventory_ui_piece())


class Monster(Base):
    def __init__(self, name=None, **kwargs) -> None:
        super().__init__(**kwargs)
        if name == None:
            self.name = self.gen_name()
        self.gen_stats()
        self.hp = self.max_hp
        self.energy = self.max_energy
        self.fill_inventory()

    def gen_name(self) -> str:
        names = [
            "Drogon",
            "Rhaegal",
            "Viserion",
            "Balerion",
            "Vhagar",
            "Meraxes",
            "Syrax",
            "Caraxes",
            "Arrax",
            "Tyraxes",
        ]
        titles = [
            "The Conqueror",
            "Firebreath",
            "The Bright",
            "The Eternal",
            "The Brave",
            "The Dark",
            "Eater of All",
            "The Chosen",
            "Sheepstealer",
            "The Stinky"
        ]
        return f"{choice(names)}, {choice(titles)}"

    def gen_stats(self) -> None:
        self.max_hp = randint(90, 140)
        self.max_energy = randint(8, 12)
        self.dmg = randint(9, 15)
        self.armor = randint(10, 20)
        self.luck = randint(12, 20)

    def fill_inventory(self) -> None:
        for _ in range(2):
            self.inventory.add_item(Item("Health Potion", 15, heal=40))
            self.inventory.add_item(Item("RedBull", 5, energy_boost=5))

    def fight(self, other):
        if self.energy < 2:
            if self.consume_item("RedBull"):
                pass
        elif self.hp < 40:
            if self.consume_item("Health Potion"):
                pass
        else:
            self.hit(other)
    
    def bounty(self):
        stats = self.hp / 10 + self.energy + self.dmg + self.armor + self.luck
        bounty = round(stats * 2)
        return int(bounty)

    def name_ui_piece(self):
        ui_str = self.name
        padding_len = 68 - len(ui_str)
        return floor(padding_len / 2) * " " + ui_str + ceil(padding_len / 2) * " "
