import random

class Card:

	# initialize card instance attrs
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def view_card(self):
		print(f'{self.rank} of {self.suit}')


class Deck:

	# initialize deck instance attrs
	def __init__(self):
		self.cardDeck = []
		self.generate_deck()
		

	def generate_deck(self):

		for i in ['D', 'H', 'C', 'S']:
			for j in range(1, 14):
				self.cardDeck.append(Card(i, j))


	def get_cards_remaining(self):
		return len(self.cardDeck)

	def shuffle(self):
		pass


if __name__ == '__main__':
	my_deck = Deck()

	for card in my_deck.cardDeck:
		card.view_card()