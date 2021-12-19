

class Item:
    def __init__(self, name: str, price: int, **kwargs) -> None:
        if not isinstance(name, str):
            raise ValueError("invalid name")
        if not isinstance(price, int):
            raise ValueError("invalid price")
        self.bonus_dmg = 0
        self.bonus_armor = 0
        self.bonus_luck = 0
        self.heal = 0
        self.energy_boost = 0
        allowed_bonuses = {
            "bonus_dmg",
            "bonus_luck",
            "bonus_armor",
            "heal",
            "energy_boost",
        }
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_bonuses)
        self.name = name
        self.price = price
        self.consumable = self.set_consumable()
        self.equippable = not self.consumable
        self.equipped = False
        try:
            self.get_bonus()
        except ValueError:
            raise NotImplementedError("items can't have more then 2 bonuses")

    def set_consumable(self) -> bool:
        if self.heal != 0 or self.energy_boost != 0:
            return True
        else:
            return False

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> int:
        return self.price
    
    def get_status(self) -> str:
        if self.consumable:
            status = "consumable"
        elif self.equippable:
            if self.equipped:
                status = "equipped"
            else:
                status = "equippable"
        return status

    def get_bonus(self) -> list:
        bonus = []
        if self.bonus_dmg:
            bonus.append(("bonus damage", self.bonus_dmg))
        if self.bonus_armor:
            bonus.append(("bonus armor", self.bonus_armor))
        if self.bonus_luck:
            bonus.append(("bonus luck", self.bonus_luck))
        if self.heal:
            bonus.append(("a heal", self.heal))
        if self.energy_boost:
            bonus.append(("an energy boost", self.energy_boost))
        if len(bonus) > 2:
            raise ValueError("item has more then 2 bonuses")
        return bonus

    def item_ui(self) -> str:
        status = self.get_status()
        effect_str = ""
        for idx, i in enumerate(self.get_bonus()):
            if len(self.get_bonus()) > 1 and idx != 0:
                effect_str += ", "
            name = i[0]
            bonus = i[1]
            effect_str += f"grants {name} of {bonus}"
        effect_str += (57 - len(effect_str)) * " "
        name_padding = (17 - len(self.name)) * " "
        price_padding = (4 - len(str(self.get_price()))) * " "
        action_padding = (21 - len(status)) * " "

        return f"""{self.get_name() + name_padding} | value per unit: {str(self.price) + price_padding} | {status + action_padding} |
| effect(s): {effect_str} |
|----------------------------------------------------------------------|"""
