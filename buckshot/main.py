from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Label, Button, Digits
from textual.reactive import var


class Buckshot(App):

    CSS_PATH = "buckshot.tcss"
    live = var("0")
    blanks = var("0")
    shells = var("33333333")
    shell_num = var(0)
    chance = var("0.0 %")

    # LOGIC

    def calculate_chance(self) -> None:
        if int(self.live) == 0 or self.shells[0] == "2":
            self.chance = "0.0 %"
            return
        if int(self.blanks) == 0 or self.shells[0] == "1":
            self.chance = "100.0 %"
            return

        unknown = self.shells.count("0")
        missing_live = int(self.live) - self.shells.count("1")
        if unknown:
            self.chance = str(round(missing_live * 100 / unknown, 1)) + " %"

    def update_shells(self, idx) -> None:
        new_val = int(self.shells[idx]) + 1
        if (
            new_val == 1
            and self.shells.count("1") == int(self.live)
            or new_val == 2
            and self.shells.count("2") == int(self.blanks)
        ):
            new_val += 1
        if new_val == 3:
            new_val = 0
        self.shells = self.shells[:idx] + str(new_val) + self.shells[idx + 1 :]
        self.auto_complete()

    def auto_complete(self):
        if int(self.live) == self.shells.count("1") + self.shells.count("0"):
            self.shells = self.shells.replace("0", "1")
        if int(self.blanks) == self.shells.count("2") + self.shells.count("0"):
            self.shells = self.shells.replace("0", "2")

    def reset_shells(self) -> None:
        for idx, state in enumerate(self.shells):
            if state != "3" and state != "0":
                self.shells = self.shells[:idx] + "0" + self.shells[idx + 1 :]

    def increase_shells(self) -> None:
        self.shell_num = int(self.live) + int(self.blanks)
        idx = self.shell_num - 1
        self.shells = self.shells[:idx] + "0" + self.shells[idx + 1 :]

    def decrease_shells(self) -> None:
        self.shell_num = int(self.live) + int(self.blanks)
        self.shells = self.shells[1:] + "3"
        self.auto_complete()

    # WATCH VARS

    def watch_live(self, live: str) -> None:
        self.query_one("#live_digits", Digits).update(live)

    def watch_blanks(self, blanks: str) -> None:
        self.query_one("#blanks_digits", Digits).update(blanks)

    def watch_shells(self, shells) -> None:
        self.query_one("#shell_str", Digits).update(shells)

        # UPDATE CHANCE
        self.calculate_chance()

        # UPDATE SHELL BUTTON CLASSES
        for idx, state in enumerate(shells):
            self.query_one(f"#shell-{idx + 1}", Button).disabled = False
            self.query_one(f"#shell-{idx + 1}", Button).remove_class(
                "live",
                "blank",
            )
            if state == "1":
                self.query_one(f"#shell-{idx + 1}", Button).add_class("live")
            if state == "2":
                self.query_one(f"#shell-{idx + 1}", Button).add_class("blank")
            if state == "3":
                self.query_one(f"#shell-{idx + 1}", Button).disabled = True

        # UPDATE +/- BUTTON CLASSES

        self.query_one("#up_live", Button).disabled = True
        self.query_one("#up_blanks", Button).disabled = True
        if self.shell_num < 8:
            self.query_one("#up_live", Button).disabled = False
            self.query_one("#up_blanks", Button).disabled = False

        self.query_one("#down_live", Button).disabled = True
        self.query_one("#down_blanks", Button).disabled = True
        if (
            shells[0] == "1"
            or int(self.live) > self.shells.count("1")
            and shells[0] != "2"
        ):
            self.query_one("#down_live", Button).disabled = False
        if (
            shells[0] == "2"
            or int(self.blanks) > self.shells.count("2")
            and shells[0] != "1"
        ):
            self.query_one("#down_blanks", Button).disabled = False

    def watch_chance(self, chance: str) -> None:
        self.query_one("#chance_digits", Digits).update(chance)
        if float(chance[:-2]) > 50:
            self.query_one("#chance_digits", Digits).add_class("high_chance")
            return
        self.query_one("#chance_digits", Digits).remove_class("high_chance")

    # COMPOSE APP

    def compose(self) -> ComposeResult:
        yield Digits(id="shell_str")

        with Container(id="chance_container"):
            yield Label("CHANCE", id="chance_label")
            yield Digits(id="chance_digits")
            with Container(id="shell_button_container"):
                for num in range(1, 9):
                    yield Button(f"{num}", id=f"shell-{num}", classes="shell_button")
                yield Button("⭯ ", id="reset")

        with Container(id="count_container"):
            with Container(id="l_container", classes="lb_container"):
                yield Label("LIVE", id="live_label")
                yield Digits(id="live_digits")
                with Container(id="l_button_container", classes="lb_button_container"):
                    yield Button("+", id="up_live", classes="up_button")
                    yield Button("-", id="down_live", classes="down_button")
            with Container(id="b_container", classes="lb_container"):
                yield Label("BLANKS", id="blanks_label")
                yield Digits(id="blanks_digits")
                with Container(id="b_button_container", classes="lb_button_container"):
                    yield Button("+", id="up_blanks", classes="up_button")
                    yield Button("-", id="down_blanks", classes="down_button")

    # BUTTON FUNCTIONALITY

    @on(Button.Pressed, "#up_live")
    def pressed_up_live(self) -> None:
        if self.shell_num == 8:
            return
        self.live = str(int(self.live) + 1)
        self.increase_shells()

    @on(Button.Pressed, "#down_live")
    def pressed_down_live(self) -> None:
        if int(self.live) == 0:
            return
        self.live = str(int(self.live) - 1)
        self.decrease_shells()

    @on(Button.Pressed, "#up_blanks")
    def pressed_up_blanks(self) -> None:
        if self.shell_num == 8:
            return
        self.blanks = str(int(self.blanks) + 1)
        self.increase_shells()

    @on(Button.Pressed, "#down_blanks")
    def pressed_down_blanks(self) -> None:
        if int(self.blanks) == 0:
            return
        self.blanks = str(int(self.blanks) - 1)
        self.decrease_shells()

    @on(Button.Pressed, ".shell_button")
    def pressed_shell(self, event: Button.Pressed) -> None:
        idx = int(event.button.id.partition("-")[-1]) - 1
        self.update_shells(idx)

    @on(Button.Pressed, "#reset")
    def pressed_reset(self) -> None:
        self.reset_shells()


if __name__ == "__main__":
    Buckshot().run()
