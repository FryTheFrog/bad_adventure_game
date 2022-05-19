from textual.views import GridView


class UI(GridView):
    def on_mount(self) -> None:
        self.grid.set_align("center", "center")
        self.grid.add_column("col", max_size=30, repeat=8)
        self.grid.add_row("row", max_size=15, repeat=8)
