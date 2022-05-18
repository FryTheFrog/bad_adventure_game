#MODIFIED VERSION OF PROGRESSBAR
#ONLY WORKS IF PLACED IN RICH FRAMEWORK FOLDER

from typing import Optional

from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import StyleType


class HealthBar(JupyterMixin):
    """Renders a health bar.

    Args:
        total (float, optional): Number of steps in the bar. Defaults to 100.
        completed (float, optional): Number of steps completed. Defaults to 0.
        width (int, optional): Width of the bar, or ``None`` for maximum width. Defaults to None.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.done".
    """

    def __init__(
        self,
        total: Optional[float] = 100.0,
        completed: float = 0,
        width: Optional[int] = None,
        style: StyleType = "bar.back",
        complete_style: StyleType = "bar.complete",
        finished_style: StyleType = "bar.finished",
    ):
        self.total = total
        self.completed = completed
        self.width = width
        self.style = style
        self.complete_style = complete_style
        self.finished_style = finished_style

    def __repr__(self) -> str:
        return f"<Bar {self.completed!r} of {self.total!r}>"

    @property
    def percentage_completed(self) -> Optional[float]:
        """Calculate percentage complete."""
        if self.total is None:
            return None
        completed = (self.completed / self.total) * 100.0
        completed = min(100, max(0.0, completed))
        return completed

    def update(self, completed: float, total: Optional[float] = None) -> None:
        """Update progress with new values.

        Args:
            completed (float): Number of steps completed.
            total (float, optional): Total number of steps, or ``None`` to not change. Defaults to None.
        """
        self.completed = completed
        self.total = total if total is not None else self.total

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:

        width = min(self.width or options.max_width, options.max_width)
        ascii = options.legacy_windows or options.ascii_only

        completed: Optional[float] = (
            min(self.total, max(0, self.completed)
                ) if self.total is not None else None
        )

        bar = "█" if ascii else "█"
        half_bar_right = " " if ascii else "▌"
        half_bar_left = " " if ascii else "▐"
        complete_halves = (
            int(width * 2 * completed / self.total)
            if self.total and completed is not None
            else width * 2
        )
        bar_count = complete_halves // 2
        half_bar_count = complete_halves % 2
        style = console.get_style(self.style)
        is_finished = self.total is None or self.completed >= self.total
        complete_style = console.get_style(
            self.finished_style if is_finished else self.complete_style
        )
        _Segment = Segment
        if bar_count:
            yield _Segment(bar * bar_count, complete_style)
        if half_bar_count:
            yield _Segment(half_bar_right * half_bar_count, complete_style)

        if not console.no_color:
            remaining_bars = width - bar_count - half_bar_count
            if remaining_bars and console.color_system is not None:
                if not half_bar_count and bar_count:
                    yield _Segment(half_bar_left, style)
                    remaining_bars -= 1
                if remaining_bars:
                    yield _Segment(bar * remaining_bars, style)

    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement:
        return (
            Measurement(self.width, self.width)
            if self.width is not None
            else Measurement(4, options.max_width)
        )
