class Evaluator:

	# initialize evaluator with cards on table and in player hands
	def __init__(self, table, players):
		self.table = table
		self.players = players

	# method to check individual player against table for flush (5 of same suit)
	def is_flush(self, player):

		# list of suits on table and in player's hand
		all_suits = [card[1] for card in self.table] + [card[1] for card in player]

		# define dictionary to store suit-level counts
		suit_counter = {}

		# iteratively populate suit count dictionary
		for suit in all_suits:
			if suit not in suit_counter:
				suit_counter[suit] = 1
			else:
				suit_counter[suit] += 1

		# if 5+  cards are the same suit, then it's a flush
		for suit in suit_counter:
			if suit_counter[suit] >= 5:

				# get all ranks present inside of the flush
				all_ranks = [card[0] for card in self.table if card[1] == suit] + [card[0] for card in player if card[1] == suit]

				# get max rank to break ties
				high_card = max(all_ranks)

				return True, high_card

		# if no flush, return false and a 0 placeholder for high card
		return False, 0

	# method to evaluate flush for all players at the table
	def evaluate_flush(self):

		# iterate over each of the players
		for i in range(len(self.players)):

			flush_exists = self.is_flush(self.players[i])

			print(i, ' Flush:', flush_exists[0], ' High:', flush_exists[1])


	def is_straight(self, player):

		all_ranks = [card[0] for card in self.table] + [card[0] for card in player]

		all_ranks = sorted(all_ranks)

		print(all_ranks)

		distances = {}

		for i in range(len(all_ranks)):

			if i != len(all_ranks) - 1:

				distances[i] = all_ranks[i + 1] - all_ranks[i]

		print(distances)



my_table = [(2, 'H'), (12, 'D'), (5, 'S'), (11, 'H'), (10, 'H')]

my_players = [[(3, 'D'), (1, 'S')], [(3, 'C'), (2, 'D')], [(9, 'H'), (6, 'H')], [(6, 'D'), (8, 'H')]]

my_eval = Evaluator(my_table, my_players)

my_eval.is_straight(my_players[0])

# my_eval.evaluate_flush()