"""
ASCII UI ELEMENTS TO BE REMOVED

unicode suits:
♠ ♥ ♦ ♣

card ASCII format:
┌─────────┐
| A       |
|         |
|    ♠    |
|         |
|       A |
└─────────┘
"""

from random import shuffle

from kivy.uix.image import Image


class Card(Image):
    hidden = False

    def __init__(self, rank: str, suit: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.rank = rank.capitalize()
        self.suit = suit.capitalize()
        self.value = self.default_val()
        self.source = self.get_image_path()

    def default_val(self) -> int:
        if self.rank.isnumeric():
            return int(self.rank)
        if self.rank == "Ace":
            return 11
        return 10

    def hide(self) -> None:
        self.hidden = True

    def reveal(self) -> None:
        self.hidden = False

    def get_image_path(self) -> str:
        return f"black_jack/src/card_assets/{self.suit.lower()}_{self.rank.lower()}.png"

    # def __repr__(self) -> str:
    #     if self.hidden:
    #         return "||||||||"
    #     return f"({self.value}) {self.rank} of {self.suit}s"


class Deck:

    RANKS = tuple((str(i) for i in range(2, 10))) + ("jack", "queen", "king", "ace")

    SUITS = ("spade", "heart", "diamond", "club")

    def __init__(self) -> None:
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self.cards.append(card)
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards != []:
            return self.cards.pop(1)
        else:
            return False

    def cards_left(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return str(self.cards)
