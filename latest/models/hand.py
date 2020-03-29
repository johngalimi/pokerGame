from deck import Deck

class Hand:
    def __init__(self):
        self.cards = []

    def receive_card(self, card):

        if len(self.cards) == 2:
            self.cards = []

        self.cards.append(card)

    def show(self):
        print('---HAND')
        for card in self.cards:
            card.show()
        print('---')


if __name__ == '__main__':
    d = Deck()
    d.show()

    h = Hand()
    h.receive_card(d.deal_card())

    d.show()

    h.show()

    h.receive_card(d.deal_card())

    d.show()
    h.show()

    h.receive_card(d.deal_card())

    d.show()
    h.show()