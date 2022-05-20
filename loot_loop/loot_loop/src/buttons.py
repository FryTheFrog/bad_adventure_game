from rich import box
from rich.panel import Panel
from rich.align import Align

from textual.reactive import Reactive
from textual.widgets import Button


class TemplateButton(Button):
    def __init__(self, label: str = "placeholder"):
        super().__init__(label.lower())

    mouse_over = Reactive(False)
    mouse_down = Reactive(False)

    def render(self) -> Panel:
        if self.mouse_over:
            return Panel(
                Align.center(self.label.capitalize(), vertical="middle"),
                style="grey50 bold" if self.mouse_down else "bold",
            )

        return Panel(Align.center(self.label.capitalize(), vertical="middle"))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
        self.mouse_down = False

    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False


class TemplateButtonFlashy(Button):
    def __init__(self, label: str = "placeholder"):
        super().__init__(label.lower())

    mouse_over = Reactive(False)
    mouse_down = Reactive(False)

    def render(self) -> Panel:
        if self.mouse_over:
            return Panel(
                Align.center(self.label.upper() + "!", vertical="middle"),
                box=box.HEAVY if self.mouse_down else box.ROUNDED,
                style="red bold" if self.mouse_down else "bold",
            )

        return Panel(Align.center(self.label.lower() + "?", vertical="middle"))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
        self.mouse_down = False

    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False


class InventoryButton(TemplateButton):
    def __init__(self):
        super().__init__("inventory")


class AttackButton(TemplateButtonFlashy):
    def __init__(self):
        super().__init__("attack")
