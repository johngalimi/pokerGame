from deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()

    def get_new_deck(self):
        self.deck = Deck()

    def deal_preflop(self, players):
        for i in range(2):
            for player in players:
                player.add_card(self.deck.deal_card())

    def deal_flop(self):
        pass



if __name__ == '__main__':
    dealer = Dealer()
    dealer.deck.show()

    dealer.get_new_deck()
    dealer.deck.show()
