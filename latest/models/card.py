import constants as const
import os

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        rank_str = const.face_card_map[self.rank] if self.rank > 10 else str(self.rank)

        print(f"{rank_str}{self.suit}")

if __name__ == "__main__":
    card = Card("S", 13)
    card.show()
       