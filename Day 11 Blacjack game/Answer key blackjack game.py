import random

def deal_card():
	"""Returns a random card from the deck"""
	card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
	return random.choice(card_values)

def calculate_score(cards):
	if sum(cards) == 21 and len(cards) == 2:
		return 0
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)
	return sum(cards)
def compare(user_score, computer_score)
user_card = []
computer_cards = []

for _ in range(2):
	user_card.append(deal_card())
	computer_cards.append(deal_card())

is_game_over = False
while not is_game_over:
	user_score = calculate_score(user_card)
	computer_score = calculate_score(user_card)
	print(f' Your cards: {user_card}, current score: {user_score}')
	print(f'Computers first card: {computer_cards[0]}')
	if user_score == 0 or computer_score == 0 or user_score > 21:
		is_game_over = True
	else:

		user_should_deal = input('Type y to get another card, type n to pass: ').lower()
		if user_should_deal == 'y':
			user_card.append(deal_card())
		else:
			is_game_over = True

	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)

#This isn't ifnished but I had the same stuff they did at the end
