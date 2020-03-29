from deck import Deck
import common.constants as const

class Dealer:
    def __init__(self):
        self.deck = Deck()

    def deal_preflop(self, players):
        for i in range(const.hand_size):
            for player in players:
                player.add_card(self.deck.deal_card())

    def burn_card(self):
        self.deck.deal_card()

    def deal_community_cards(self, is_flop):
        self.burn_card()
        num_cards = const.flop_size if is_flop else const.turn_or_river_size

        return [self.deck.deal_card() for card in range(num_cards)]

    def get_new_deck(self):
        self.deck = Deck()


if __name__ == '__main__':
    dealer = Dealer()
    dealer.deck.show()

    dealer.get_new_deck()
    dealer.deck.show()
