from player import Player
from dealer import Dealer

class Table:
    def __init__(self, players, blind):
        self.players = players
        self.community_cards = []
        self.pot = 0
        self.small_blind = blind
        self.big_blind = 2 * blind

    def receive_chips(self, chips):
        self.pot += chips

    def add_community_cards(self, cards):
        self.community_cards.extend(cards)

    def show_table(self):
        print('---TABLE')

        remaining_players = [player.id for player in self.players]
        print('Remaining Players: ', remaining_players)

        print(f'Blinds: {self.small_blind}/{self.big_blind}')
        print('Pot: ', self.pot)

        print('Community Cards:')
        for card in self.community_cards:
            card.show()

        print('---')


if __name__ == '__main__':
    p1 = Player(1, 1000)
    p2 = Player(2, 1500)

    t = Table([p1, p2], 10)

    d = Dealer()
    d.deck.show()

    d.deal_preflop(t.players)

    for player in t.players:
        player.show_hand()

    d.deck.show()

    t.add_community_cards(d.deal_community_cards(True))
    t.add_community_cards(d.deal_community_cards(False))
    t.add_community_cards(d.deal_community_cards(False))

    t.show_table()