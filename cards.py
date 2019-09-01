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


if __name__ == '__main__':
	
	my_deck = Deck()

	my_deck.view_deck()

	print('-----------dealing')

	dealt_1 = my_deck.deal_card()
	dealt_2 = my_deck.deal_card()

	dealt_1.view_card()
	dealt_2.view_card()

	print(my_deck.get_cards_remaining())