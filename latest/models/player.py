from hand import Hand
from deck import Deck

class Player:
    def __init__(self, id, buy_in):
        self.id = id
        self.chips = buy_in
        self.hand = Hand()
    
    def update_chips(self, amount):
        pending_value = self.chips + amount
        self.chips = pending_value if pending_value >= 0 else 0

    def show_chips(self):
        print(self.chips)

    def show_hand(self):
        self.hand.show()

    def add_card(self, card):
        self.hand.receive_card(card)


if __name__ == '__main__':
    p = Player(1, 100)

    p.show_chips()

    p.update_chips(200)
    p.show_chips()

    p.update_chips(-350)
    p.show_chips()

    p.update_chips(71)
    p.show_chips()

    p.show_hand()

    d = Deck()
    d.show()

    p.add_card(d.deal_card())
    p.add_card(d.deal_card())

    p.show_hand()

    p.add_card(d.deal_card())

    p.show_hand()

    p.add_card(d.deal_card())

    p.show_hand()

    d.show()

