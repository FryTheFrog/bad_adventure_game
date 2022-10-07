"""
♠ ♥ ♦ ♣

BLACK JACK

♠ ♥ ♦ ♣
"""

from src.logic import Round
from src.player import Player
from src.cards import Deck

from kivy.app import App
from kivy.properties import NumericProperty, StringProperty
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

# DEBUGGING PURPOSE IMPORTS
from kivy.uix.button import Button


class MenuBarWidget(StackLayout):
    size_hint = None, None
    size = dp(450), dp(30)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for _ in range(3):
            self.add_widget(
                Button(
                    text="PLACEHOLDER", size_hint=(None, None), size=(dp(150), dp(30))
                )
            )


class Hand(BoxLayout):
    def __init__(self, cards: list, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        for card in cards:
            self.count += 1
            self.add_widget(card)
        self.size_hint_x = self.count * 0.1


class HandWidget(AnchorLayout):
    def __init__(self, cards: list, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Hand(cards))


class Infos(BoxLayout):
    orientation = "vertical"
    size_hint = None, None
    size = dp(150), dp(40)

    def __init__(self, player: Player, round: Round, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(
            Label(
                text=f"Stake: {round.stake} $",
                size_hint=(None, None),
                size=(dp(150), dp(20)),
            )
        )
        self.add_widget(
            Label(
                text=f"Bank: {player.bank} $",
                size_hint=(None, None),
                size=(dp(150), dp(20)),
            )
        )


class InfoWidget(AnchorLayout):
    size_hint = 1, 0.2

    def __init__(self, player: Player, round: Round, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Infos(player, round))


class ControlsWidget(BoxLayout):
    size_hint = 1, 0.5
    padding = 60, 20, 60, 20
    spacing = 20

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for _ in range(3):
            self.add_widget(Button(text="PLACEHOLDER"))


class Master(BoxLayout):
    orientation = "vertical"

    deck = Deck()
    player = Player()
    round = None

    info_box = None
    player_hand = None
    dealer_hand = None
    controls = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_round()
        self.round.deal()
        for card in self.player.hand:
            print(card.source)
        self.update_all()

        self.add_widget(MenuBarWidget())
        self.add_widget(self.player_hand)
        self.add_widget(self.dealer_hand)
        self.add_widget(self.info_box)
        self.add_widget(ControlsWidget())

    def init_round(self):
        if self.deck.cards_left() < 13:
            self.deck = Deck()
        self.player.reset_hand()
        self.round = Round(self.deck, self.player)

    def update_all(self):
        self.player_hand = HandWidget(self.player.hand)
        self.dealer_hand = HandWidget(self.round.dealer.hand)
        self.info_box = InfoWidget(self.player, self.round)


class BlackJackApp(App):
    pass


BlackJackApp().run()
