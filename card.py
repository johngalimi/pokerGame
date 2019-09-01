class Card:

	# initialize instance attrs
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	# get rank method
	def get_rank(self):
		return self.rank

	# get suit method
	def get_suit(self):
		return self.suit


if __name__ == '__main__':
	my_card = Card('d', 2)

	print(my_card)

	print(my_card.get_rank())

	print(my_card.get_suit())
