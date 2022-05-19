from rich import box
from rich.panel import Panel
from rich.align import Align

from textual.reactive import Reactive
from textual.widgets import Button

class BasicButton(Button):
    def __init__(self):
        super().__init__("BASIC")
    mouse_over = Reactive(False)
    mouse_down = Reactive(False)

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
        self.mouse_down = False

    def on_mouse_down(self) -> None:
        self.mouse_down = True

    def on_mouse_up(self) -> None:
        self.mouse_down = False
