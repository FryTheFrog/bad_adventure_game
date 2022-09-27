"""
ASCII UI TO BE REMOVED

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


class Card:

    SUIT_SYMBOL = {"spade": "♠", "heart": "♥", "diamond": "♦", "club": "♣"}

    CARD = """\
┌─────────┐
| {}      |
|         |
|    {}    |
|         |
|      {} |
└─────────┘""".format(
        "{rank: <2}", "{suit}", "{rank: >2}"
    )

    HIDDEN_CARD = """\
┌─────────┐
| ▒░▒░▒░▒ |
| ▒░▒░▒░▒ |
| ▒░▒░▒░▒ |
| ▒░▒░▒░▒ |
| ▒░▒░▒░▒ |
└─────────┘"""

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank.capitalize()
        self.suit = suit.capitalize()
        self.symbol = self.SUIT_SYMBOL[suit.lower()]
        self.hidden = False
        self.value = self.default_val()

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

    def card_ascii(self) -> str:
        if self.hidden:
            return self.HIDDEN_CARD
        rank = self.rank if self.rank == "10" else self.rank[0]
        return self.CARD.format(rank=rank, suit=self.symbol)

    def __repr__(self) -> str:
        if self.hidden:
            return "||||||||"
        return f"({self.value}) {self.rank} of {self.suit}s"


class Deck:

    RANKS = tuple((str(i) for i in range(1, 10))) + ("jack", "queen", "king", "ace")

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
