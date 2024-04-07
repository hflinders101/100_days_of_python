import random

card_values = [11,2,3,4,5,6,7,8,9,10,10,10]

def score_determiner(your_hand,dealer):
	""""This will figure out who won at any given time"""
	if sum(dealer) > 21:
		print(f'The dealer busted with {dealer}, you win with {your_hand}')
		return False
	elif sum(dealer) > sum(your_hand):
		print(f'You lose, your hand is {your_hand} and the dealer had {dealer}')
		return False
	elif sum(dealer) == sum(your_hand):
		print(f"It's a draw. You had {your_hand} and the dealer had {dealer}")
		return False
	elif 11 in your_hand and 10 in your_hand and 11 in dealer and 10 in dealer:
		print("You and the dealer got blackjack. It's a draw")
	elif 11 in your_hand and 10 in your_hand:
		print(f'You got blackjack with {your_hand}')
	elif 11 in dealer and 10 in dealer:
		print(f'The dealer got blackjack with {dealer}')
	else:
		print(f'You won with {your_hand} against the dealer had of {dealer}')
		return False
def hit_or_stand(your_hand,dealer):
	play_decision = input('Type "h" for hit and "s" for stand ').lower()
	while sum(dealer) < 16:
		dealer.append(random.choice(card_values))
	if play_decision == 'h':
		your_hand.append(random.choice(card_values))
		if sum(your_hand) > 21:
			print(f'You lose, your hand is {your_hand} and the dealer had {dealer}')
			return False
		else:
			print(f'Your hand is {your_hand}')
			return score_determiner(your_hand,dealer)
	else:
		return score_determiner(your_hand,dealer)

def black_jack():
	continue_game = True
	dealer = []
	your_hand = []

	dealer.append(random.choice(card_values))
	print(f'The hand of the dealer contains {dealer}')
	your_hand.extend((random.choice(card_values), random.choice(card_values)))
	print(f'Your hand is {your_hand}')

	while continue_game:
		continue_game = hit_or_stand(your_hand,dealer)
	play_again = input("Play again? Type 'y' or 'n' ").lower()
	if play_again == 'y':
		black_jack()
black_jack()

#Need to add another hit