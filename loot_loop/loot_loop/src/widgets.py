from rich import box
from rich.panel import Panel
from rich.healthbar import HealthBar
from rich.align import Align

from textual.reactive import Reactive
from textual.widget import Widget
from textual.views import DockView
from textual.events import Focus, Blur


class HpBar(Widget):
    def __init__(self, name: str, max: int, cur: int) -> None:
        super().__init__()
        self.name = name
        self.max = max

    # change this value to update the bar
    cur = Reactive(100)

    bar = HealthBar(completed=100, finished_style="bar.complete")
    mouse_over = Reactive(False)

    def watch_cur(self, cur: int) -> None:
        self.bar = HealthBar(
            total=self.max, completed=self.cur, finished_style="bar.complete"
        )

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def render(self) -> Panel:
        return Panel(
            self.bar,
            title="Hit Points" if self.mouse_over else f"[b]{self.name}[/b]",
            subtitle=str(self.cur) if self.mouse_over else "",
            style="bold" if self.mouse_over else "none",
            height=3,
        )


class EnergyBar(Widget):
    def __init__(self, max: int, cur: int) -> None:
        super().__init__()
        self.max = max

    # change this value to update the bar
    cur = Reactive(100)

    bar = HealthBar(completed=100, complete_style="bar.finished")
    mouse_over = Reactive(False)

    def watch_cur(self, cur: int) -> None:
        self.bar = HealthBar(
            total=self.max, completed=self.cur, complete_style="bar.finished"
        )

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def render(self) -> Panel:
        return Panel(
            self.bar,
            title="Energy" if self.mouse_over else "",
            subtitle=str(self.cur) if self.mouse_over else "",
            style="bold" if self.mouse_over else "none",
            height=3,
        )


class ItemEntry(Widget):
    def __init__(self, name: str, value: int, bonus: str) -> None:
        super().__init__(name)
        self.value = value
        self.bonus = bonus

    has_focus = Reactive(False)
    mouse_over = Reactive(False)

    def render(self) -> Panel:
        if self.mouse_over:
            return Panel(
                Align.center(
                    f"{self.name} (value: {self.value})\nbonuses: {self.bonus}"
                ),
                box=box.HEAVY if self.has_focus else box.ROUNDED,
                style="blue bold" if self.has_focus else "bold",
                height=4,
            )
        return Panel(
            Align.center(f"{self.name} (value: {self.value})"),
            box=box.SIMPLE,
            height=3,
        )

    def on_focus(self, event: Focus) -> None:
        self.has_focus = True

    def on_blur(self, event: Blur) -> None:
        self.has_focus = False

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
