from hand import Hand

class Player:
    def __init__(self, buy_in):
        self.chips = buy_in
        self.hand = Hand()
    
    def update_chips(self, amount):

        pending_value = self.chips + amount
        self.chips = pending_value if pending_value >= 0 else 0

    def show_chips(self):
        print(self.chips)


if __name__ == '__main__':
    p = Player(100)

    p.show_chips()

    p.update_chips(200)
    p.show_chips()

    p.update_chips(-350)
    p.show_chips()

    p.update_chips(71)
    p.show_chips()

    p.update_chips(-70)
    p.show_chips()

    p.update_chips(-555)
    p.show_chips()

    p.update_chips(-12)
    p.show_chips()

    p.update_chips(1000)
    p.show_chips()
