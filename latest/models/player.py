from hand import Hand

class Player:
    def __init__(self, buy_in):
        self.chips = buy_in
        self.hand = Hand()
    
    def update_chips(self, amount):
        self.chips += amount

    def show_chips(self):
        print(self.chips)


if __name__ == '__main__':
    p = Player(100)
