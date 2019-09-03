import random

class Card:

	# initialize card instance attrs
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	# method to view card attributes
	def view_card(self):
		print(f'{self.rank} of {self.suit}')


class Deck:

	# initialize deck instance attrs
	def __init__(self):
		self.cardDeck = []
		self.generate_deck()
		self.shuffle_deck()
		
	# method to generate deck
	def generate_deck(self):
		for i in ['D', 'H', 'C', 'S']:
			for j in range(1, 14):
				self.cardDeck.append(Card(i, j))

	# method to shuffle deck
	def shuffle_deck(self):
		random.shuffle(self.cardDeck)

	# method to get num cards remaining - check when dealing
	def get_cards_remaining(self):
		return len(self.cardDeck)

	# method to view entire deck
	def view_deck(self):
		for deck_card in self.cardDeck:
			deck_card.view_card()

	# method to deal single card
	def deal_card(self):
		return self.cardDeck.pop()


class Player:

	# initialize player instance attrs
	def __init__(self, player, chips):
		self.player = player
		self.chips = chips
		self.hand = []
		self.wager = 0

	# method for player to receive dealt cards
	def receive_card(self, deck):
		self.hand.append(deck.deal_card())

	# method to view player hand
	def view_hand(self):
		for player_card in self.hand:
			player_card.view_card()

	# method to add on to total amt wagered
	def make_bet(self, bet):
		self.wager += bet
		self.chips -= bet

		# need to set hand wager to 0 for each player after bets are in
		# self.wager = 0


class Hand:

	# initialize hand instance attr
	def __init__(self):
		self.table_cards = []


	def view_table(self):

		print('----Table----')

		for table_card in self.table_cards:
			table_card.view_card()


	def deal_flop(self, deck):

		flop_cards = 3

		while flop_cards > 0:
			self.table_cards.append(deck.deal_card())

			flop_cards -= 1


	def deal_turn_or_river(self, deck):

		self.table_cards.append(deck.deal_card())


class Game:

	pass


if __name__ == '__main__':
	
	my_deck = Deck()

	my_deck.view_deck()

	print('--------starting')

	john = Player('john', 100)

	john.receive_card(my_deck)
	john.receive_card(my_deck)

	john.view_hand()

	print(john.chips)

	john.make_bet(7)

	print(john.wager)
	print(john.chips)

	my_hand = Hand()

	my_hand.deal_flop(my_deck)

	my_hand.view_table()

	my_hand.deal_turn_or_river(my_deck)

	my_hand.view_table()

	my_hand.deal_turn_or_river(my_deck)

	my_hand.view_table()

	print(my_deck.get_cards_remaining())