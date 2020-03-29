import constants as const
from card import Card

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
    
    def generate_deck(self):

        deck = []

        for suit in const.suits:
            for rank in list(range(2, 15)):
                deck.append(Card(suit, rank))

        for card in deck:
            card.show_card()

        print(len(deck))


if __name__ == "__main__":
    d = Deck()