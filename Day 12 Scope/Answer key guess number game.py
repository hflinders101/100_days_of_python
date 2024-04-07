from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
	if guess > answer:
		print('Too high')
		return turns -1
	elif guess < answer:
		print('Too low')
		return turns -1
	else:
		print(f'You win! The answer was {answer}')

def set_difficulty():
	level = input('Choose a diff, easy or hard').lower()
	if level == 'easy':
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS

def game():
	answer = randint(1,100)
	print("I'm thinking of a number between 1 and 100")
	print(f'The answer is {answer}')
	turns = set_difficulty()

	guess = 0
	while guess != answer:
		guess = int(input("Make a guess: "))
		turns = check_answer(guess, answer, turns)
		print(f'You have {turns} attempts left.')
		if turns == 0:
			print(f'You lose, the answer is {answer}')
			return

game()