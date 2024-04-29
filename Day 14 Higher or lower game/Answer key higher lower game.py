from Data import data
import random


def format_date(account):
	account_name = account['name']
	account_descr = account['description']
	account_country = account['country']
	return (f'{account_name}, a {account_descr}, from {account_country}')
	#I didn't know you could return a string like this and fit it into the output


def check_answer(guess,a_followers, b_followers):
	"""Takes user guess and followers and retunrs which is right (T or F)"""
	if a_followers > b_followers:
		return guess == 'a' #This will return true if guess is equal to 'a', false likewise
	else:
		return guess == 'b'


score = 0

game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
	account_a = account_b #Using random.choice was better than index which is what I did

	while account_a == account_b:
		account_b = random.choice(data)

	print(f'compare A: {format_date(account_a)}.')
	print(f'against B: {format_date(account_b)}.')

	guess = input('Who has more followers? A or B?').lower()

	a_follower_count = account_a['follower_count']
	b_follower_count = account_b['follower_count']
	is_correct = check_answer(guess, a_follower_count,b_follower_count)
	if is_correct:
		score += 1
		print(f'Correct. You score is {score}')
	else:
		print(f'That is wrong. Your score is {score}')
		game_should_continue = False