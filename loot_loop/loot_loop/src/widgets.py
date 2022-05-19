from rich.panel import Panel
from rich.healthbar import HealthBar

from textual.reactive import Reactive
from textual.widget import Widget

from entities import Entity


class HpBar(Widget):
    def __init__(self, entity: Entity, name: str | None = None) -> None:
        super().__init__(name)
        name = entity.name
        max = entity.max_hp
        bar = Reactive(HealthBar(
            total=entity.max_hp,
            completed=entity.hp))
        hp = Reactive(entity.hp)

    mouse_over = Reactive(False)

    def watch_hp(self, hp: int):
        self.bar = HealthBar(
            total=self.max,
            completed=self.hp
        )

    def render(self):
        return Panel(self.bar,
                     title="Hit Points" if self.mouse_over else self.name,
                     subtitle=str(self.hp) if self.mouse_over else "",
                     style="bold" if self.mouse_over else "none",
                     height=3)

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
