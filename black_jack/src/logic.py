from cards import Deck
from player import Player, Dealer


class Round:
    def __init__(self, deck: Deck, player: Player) -> None:
        self.deck = deck
        self.stake = 0
        self.player = player
        self.double = False
        self.dealer = Dealer()

    def bet(self, amount: int) -> None:
        if amount > self.player.bank:
            return
        self.player.bank -= amount
        self.stake += amount

    def deal(self) -> None:
        for _ in range(2):
            self.player.add_to_hand(self.deck.draw_card())
            self.dealer.add_to_hand(self.deck.draw_card())

    def play(self, choice: str) -> None:
        if choice not in self.player.allowed_plays():
            raise Warning("this move is impossible")
        if choice in ["hit", "double"]:
            card = self.deck.draw_card()
            self.player.add_to_hand(card)
        if choice == "double" and not self.double:
            self.double = True
            self.bet(self.stake)

    def dealers_play(self) -> None:
        choice = self.dealer.get_choice()
        while choice != "stand":
            card = self.deck.draw_card()
            self.dealer.add_to_hand(card)
            choice = self.dealer.get_choice()

    def check_winner(self) -> str:
        if self.player.check_bust():
            return "dealer"
        if self.dealer.check_bust():
            return "player"
        if self.player.check_blackjack():
            if self.dealer.check_blackjack():
                return None
            return "player"
        if self.dealer.check_blackjack():
            return "dealer"
        return None

    def find_winner(self) -> str:
        winner = self.check_winner()
        if winner:
            return winner
        if self.player.get_score() > self.dealer.get_score():
            return "player"
        if self.dealer.get_score() > self.player.get_score():
            return "dealer"
        return "push"

    def settlement(self) -> int:
        if self.find_winner() == "player":
            if self.player.check_blackjack():
                amount = self.stake + int(self.stake * 1.5 // 1)
                self.player.bank += amount
                return amount
            self.player.bank += self.stake * 2
            return self.stake * 2
        if self.find_winner() == "push":
            self.player.bank += self.stake
            return self.stake
        return 0


# DEBUGGING FUNCTIONALITY ONLY
class DebugGame:
    def __init__(self) -> None:
        self.deck = Deck()
        self.player = Player()
        self.round = None

    def play_round(self):

        # initialize round
        if self.deck.cards_left() < 13:
            self.deck = Deck()
        if self.player.bank <= 0:
            self.player = Player()
            print("player has been reset")
        self.player.reset_hand()
        self.round = Round(self.deck, self.player)

        print("--------------------")
        print(self)

        # bet
        while self.round.stake == 0:
            print("choose bet")
            stake = int(input("> "))
            self.round.bet(stake)

        # deal phase
        self.round.deal()

        # natural
        if self.round.check_winner():
            self.round.settlement()
            print(f"\n{self}")
            print(f"{self.round.check_winner()} won!")
            return
        player_inp = None

        # play phase
        while player_inp != "stand" and not self.round.check_winner():
            print(f"\n{self}")
            print("your move")
            player_inp = input("> ")
            self.round.play(player_inp)

        # dealer's play
        self.round.dealer.reveal_hand()
        if self.round.check_winner():
            self.round.settlement()
            print(f"\n{self}")
            print(f"{self.round.check_winner()} won!")
            return
        self.round.dealers_play()

        # settlement
        self.round.settlement()

        print(f"\n{self}")
        print(f"{self.round.find_winner()} won!")

    def __repr__(self) -> str:
        return f"""dealer: {self.round.dealer.get_score()} {self.round.dealer.hand}
player: {self.player.get_score()} {self.player.hand}
bank: {self.player.bank}"""


if __name__ == "__main__":
    game = DebugGame()
    while True:
        game.play_round()
