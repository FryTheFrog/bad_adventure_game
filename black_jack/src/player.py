from src.cards import Card


class Player:
    def __init__(self, bank: int = 1000) -> None:
        self.bank = bank
        self.hand = []

    def get_score(self) -> int:
        score = 0
        for card in self.hand:
            if not card.hidden:
                score += card.value
        if score <= 21:
            return score
        for card in self.hand:
            if card.rank == "Ace" and card.value == 11 and not card.hidden:
                card.value = 1
                return self.get_score()
        return score

    def allowed_plays(self) -> list:
        allowed = ["stand"]
        if self.get_score() < 21:
            allowed.extend(("hit", "double"))
        return allowed

    def check_blackjack(self) -> bool:
        if len(self.hand) == 2 and self.get_score() == 21:
            return True
        return False

    def check_bust(self) -> bool:
        if self.get_score() > 21:
            return True
        return False

    def reset_ace_vals(self) -> None:
        for card in self.hand:
            if card.rank == "Ace":
                card.value = 11

    def reset_hand(self) -> None:
        self.hand = []

    def add_to_hand(self, card: Card) -> None:
        self.hand.append(card)


class Dealer(Player):
    def add_to_hand(self, card: Card) -> None:
        if self.hand == []:
            card.hide()
        self.hand.append(card)

    def reveal_hand(self):
        self.hand[0].reveal()

    def get_choice(self):
        if self.get_score() < 17:
            return "hit"
        return "stand"
