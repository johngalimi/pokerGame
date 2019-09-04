import random
from evaluator import Evaluator

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
			for j in range(2, 15):
				self.cardDeck.append(Card(i, j))

	# method to shuffle deck
	def shuffle_deck(self):
		random.shuffle(self.cardDeck)

	# method to get num cards remaining - check when dealing
	def get_cards_remaining(self):
		print(len(self.cardDeck))

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

		print(f'----Hand: {self.player}----')

		for player_card in self.hand:
			player_card.view_card()

	# method to add on to total amt wagered
	def make_bet(self, bet):
		self.wager += bet
		self.chips -= bet

		# need to set hand wager to 0 for each player after bets are in
		# self.wager = 0


class Hand:

	# initialize hand instance attrs
	def __init__(self, player_list):
		self.player_list = player_list
		self.table_cards = []
		self.pot = 0

	# method to initially deal cards
	def initial_deal(self, deck):

		# refactor to elim nested for loop to cycle thru player list twice on deal
		for i in range(2):
			for player in self.player_list:
				player.receive_card(deck)

	# method to view cards currently on the table
	def view_table(self):

		print('----Table----')

		for table_card in self.table_cards:
			table_card.view_card()

	# method to deal first three table cards, the "flop"
	def deal_flop(self, deck):

		flop_cards = 3

		while flop_cards > 0:
			self.table_cards.append(deck.deal_card())
			flop_cards -= 1

	# method to deal either the 4th (turn) or 5th (river) card
	def deal_turn_or_river(self, deck):
		self.table_cards.append(deck.deal_card())

	# method to evaluate hands to find winner
	def evaluate_hands(self):

		# create list of table cards as individual tuples
		table = [(i.rank, i.suit) for i in self.table_cards]

		players = []

		# create list of lists for player cards as tuples
		for player in self.player_list:
			players.append([(i.rank, i.suit) for i in player.hand])

		print('----Evaluating')

		# create instance of hand evaluator
		hand_evaluator = Evaluator(table, players)

		# check for flush
		hand_evaluator.evaluate_flush()


class Game:

	# initialize Game instance attrs
	def __init__(self, num_players, starting_chips):
		# when a player gets knocked out, the number of players piped into a given instance of Hand will be decremented
		self.num_players = num_players
		self.starting_chips = starting_chips

	# method to create all players for the game
	def create_players(self):

		player_holder = {}

		for i in range(self.num_players):
			player_holder[i] = Player(i, self.starting_chips)

		player_list = list(player_holder.values())

		return player_list


if __name__ == '__main__':
	
	my_game = Game(4, 100)

	my_players = my_game.create_players()

	my_hand = Hand(my_players)

	my_deck = Deck()

	my_deck.get_cards_remaining()

	my_hand.initial_deal(my_deck)

	# maybe method to view all players at a table
	for player in my_players:
		player.view_hand()
		print(player.chips)

	my_hand.deal_flop(my_deck)

	my_hand.deal_turn_or_river(my_deck)

	my_hand.deal_turn_or_river(my_deck)

	my_hand.view_table()

	my_hand.evaluate_hands()

