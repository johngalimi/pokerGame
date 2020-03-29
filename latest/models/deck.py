import constants as const
import random

from card import Card

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
    
    def generate_deck(self):

        deck = []

        for suit in const.suits:
            for rank in list(range(2, 15)):
                deck.append(Card(suit, rank))

        random.shuffle(deck)
        
        return deck

if __name__ == "__main__":
    d = Deck()

    for card in d.cards:
        card.show_card()

    print(len(d.cards))