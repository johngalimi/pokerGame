class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show_card(self):

        face_card_map = {
            11: "J",
            12: "Q",
            13: "K",
            14: "A"
        }

        rank_str = face_card_map[self.rank] if self.rank > 10 else str(self.rank)

        print(f"{rank_str}{self.suit}")

if __name__ == "__main__":
    card = Card(13, "S")
    card.show_card()
       