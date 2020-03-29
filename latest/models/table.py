from player import Player
from dealer import Dealer

class Table:
    def __init__(self, players, blind):
        self.players = players
        self.community_cards = []
        self.pot = 0
        self.small_blind = blind
        self.big_blind = 2 * blind
        self.is_game_over = False

    def receive_chips(self, chips):
        self.pot += chips

    def add_community_cards(self, cards):
        self.community_cards.extend(cards)

    def check_table_state(self):
        for player in self.players:
            if player.chips == 0:
                print(f'Removing Player ID: {player.id}')
                self.players.remove(player)

        if len(self.players) == 1:
            print(f'Winner! Player ID: {self.players[0].id}')
            self.is_game_over = True

    def show_table(self):
        print('---TABLE')

        remaining_players = [(player.id, player.chips) for player in self.players]
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
    p3 = Player(3, 200)

    t = Table([p1, p2, p3], 10)

    d = Dealer()

    d.deal_preflop(t.players)

    for player in t.players:
        player.show_hand()

    t.add_community_cards(d.deal_community_cards(True))
    t.add_community_cards(d.deal_community_cards(False))
    t.add_community_cards(d.deal_community_cards(False))

    t.show_table()

    p3.update_chips(-300)

    t.check_table_state()

    t.show_table()

    p2.update_chips(-1500)

    t.show_table()

    t.check_table_state()

    t.show_table()