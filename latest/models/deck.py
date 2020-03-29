import constants as const
import random

from card import Card

class Deck:
    def __init__(self):
        self.cards = self.generate()
    
    def generate(self):

        deck = []

        for suit in const.suits:
            for rank in list(range(2, 15)):
                deck.append(Card(suit, rank))

        random.shuffle(deck)

        return deck

    def deal_card(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            card.show()

        print("CARDS REMAINING:", len(self.cards))


if __name__ == "__main__":
    d = Deck()

    d.show()

    card = d.deal_card()

    print("DEALT CARD:")
    card.show()

    d.show()