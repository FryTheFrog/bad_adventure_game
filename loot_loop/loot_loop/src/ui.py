from src.entities import Entity, Player
from src.buttons import InventoryButton, AttackButton

from textual.views import GridView
from textual.widgets import Button, ButtonPressed


class UI(GridView):
    def on_mount(self) -> None:
        self.grid.set_align("center", "center")
        self.grid.add_column("col", max_size=30, repeat=8)
        self.grid.add_row("row", max_size=15, repeat=8)

        self.inv_button = InventoryButton()

        self.grid.add_areas(inv_button="col8,row8")

        self.grid.place(inv_button=self.inv_button)

    def handle_button_pressed(self, event: ButtonPressed):
        assert isinstance(event.sender, Button)
        button_name = event.sender.name

        if button_name == "inventory":
            pass


class BattleUI(UI):
    def __init__(self, player: Player, enemy: Entity) -> None:
        super().__init__()
        self.player = player
        self.enemy = enemy
        self.check_fighters()

    def check_fighters(self):
        assert isinstance(self.player, Entity)
        assert isinstance(self.enemy, Entity)
        self.player.update_attr()
        self.enemy.update_attr()

    def handle_button_pressed(self, event: ButtonPressed) -> None:
        button_name = event.sender.name

        if button_name == "attack":
            self.player.attack(self.enemy)

    def on_mount(self) -> None:
        self.atk_button = AttackButton()
        self.grid.add_areas(
            enemy_hp_bar="col2-start|col7-end,row2",
            player_hp_bar="col1-start|col3-end,row7",
            player_en_bar="col1-start|col3-end,row8",
            atk_button="col4-start|col5-end,row8",
        )

        self.grid.place(
            enemy_hp_bar=self.enemy.hp_bar,
            player_hp_bar=self.player.hp_bar,
            player_en_bar=self.player.en_bar,
            atk_button=self.atk_button,
        )
