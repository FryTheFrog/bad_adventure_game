from pickle import NONE
from rich import box
from rich.panel import Panel
from rich.align import Align
from rich.healthbar import HealthBar

from textual.app import App
from textual.events import Action
from textual.views import GridView
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Button, ButtonPressed


class Entity:
    def __init__(self) -> None:
        self.health = 100
        self.hp_bar = HitPoints()
        self.is_dead = False

    def update_hp_bar(self) -> None:
        if self.health < 0:
            self.health = 0
        self.hp_bar.val = self.health

    def reset(self) -> None:
        self.health = 100
        self.is_dead = False
        self.update_hp_bar()

    def attack(self, other) -> None:
        other.health -= 10
        other.update_hp_bar()


class Player(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Player"


class Enemy(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Enemy"


class GameOver(Action):
    pass


class HitPoints(Widget):
    mouse_over = Reactive(False)
    val = Reactive(100)
    bar = Reactive(HealthBar(completed=100))
    dead = Reactive(False)

    def watch_val(self, value: int) -> None:
        self.bar = HealthBar(completed=self.val)
        if self.val <= 0:
            self.dead = True

    def render(self) -> None:
        if self.dead:
            return Panel(
                self.bar,
                title="Dead Enemy",
                subtitle="You Won!",
                style="bold",
                height=3,
            )
        return Panel(
            self.bar,
            title="Hit Points" if self.mouse_over else "Enemy",
            subtitle=str(self.val) if self.mouse_over else "",
            style="bold" if self.mouse_over else "none",
            height=3,
        )

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class AttackButton(Button):
    def __init__(self) -> None:
        super().__init__("ATTACK")

    mouse_over = Reactive(False)
    mouse_down = Reactive(False)

    def render(self) -> Panel:
        if self.mouse_over:
            return Panel(
                Align.center("ATTACK!", vertical="middle"),
                box=box.HEAVY if self.mouse_down else box.ROUNDED,
                style="red bold" if self.mouse_down else "bold",
                border_style="red" if self.mouse_down else "none",
            )
        else:
            return Panel(Align.center("attack?", vertical="middle"))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
        self.mouse_down = False

    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False


class ResetButton(Button):
    def __init__(self) -> None:
        super().__init__("RESET")

    mouse_over = Reactive(False)
    mouse_down = Reactive(False)

    def render(self) -> Panel:
        if self.mouse_over:
            return Panel(
                Align.center("RESET!", vertical="middle"),
                box=box.HEAVY if self.mouse_down else box.ROUNDED,
                style="red bold" if self.mousedown else "bold",
                border_style="red" if self.mouse_down else "none",
            )
        else:
            return Panel(Align.venter("reset?", vertical="middle"))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
        self.mouse_down = False

    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False


class BattleUI(GridView):
    def handle_button_pressed(self, event: ButtonPressed) -> None:
        assert isinstance(event.sender, Button)
        button_name = event.sender.name
        if button_name == "ATTACK":
            self.player.attack(self.enemy)
        elif button_name == "RESET":
            self.player.reset()
            self.enemy.reset()

    def on_mount(self) -> None:
        self.player = Player()
        self.enemy = Enemy()
        self.atk_button = AttackButton()
        self.reset_button = ResetButton()
        self.hp_bar = self.enemy.hp_bar

        self.grid.set_align("center", "center")

        self.grid.add_column("col", max_size=30, repeat=8)
        self.grid.add_row("row", max_size=15, repeat=8)
        self.grid.add_areas(
            hp_bar="col2-start|col7-end,row3",
            button="col3-start|col6-end,row5-start|row6-end",
        )

        self.grid.place(hp_bar=self.hp_bar, button=self.atk_button)


class GameOverUI(GridView):
    def handle_button_pressed(self, event: ButtonPressed) -> None:
        assert isinstance(event.sender, Button)
        button_name = event.sender.name
        if button_name == "RESET":
            self.player.reset()
            self.enemy.reset()

    def on_mount(self) -> None:
        self.player = Player()
        self.enemy = Enemy()
        self.atk_button = AttackButton()
        self.reset_button = ResetButton()
        self.hp_bar = self.enemy.hp_bar

        self.grid.set_align("center", "center")

        self.grid.add_column("col", max_size=30, repeat=8)
        self.grid.add_row("row", max_size=15, repeat=8)
        self.grid.add_areas(
            hp_bar="col2-start|col7-end,row3",
            button="col3-start|col6-end,row5-start|row6-end",
        )

        self.grid.place(hp_bar=self.hp_bar, button=self.reset_button)


class Attacker(App):
    async def on_load(self) -> None:
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")

    async def on_mount(self) -> None:
        await self.view.dock(BattleUI())

    async def on_event(self, event: events.Event) -> None:
        return await super().on_event(event)


Attacker.run()
