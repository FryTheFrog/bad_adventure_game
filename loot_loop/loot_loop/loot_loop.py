# ONLY DEBUGGING FUNCTIONALITY

from src.ui import BattleUI
from src.entities import Player, Entity

from textual.app import App

# LAZY IMPORTS
from src.items import Consumable


class LootLoop(App):
    p = Player()
    p.inv.add_item(Consumable("redbull", 3))


    async def on_load(self) -> None:
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")

    async def on_mount(self) -> None:
        await self.view.dock(self.item_list)


LootLoop.run()
