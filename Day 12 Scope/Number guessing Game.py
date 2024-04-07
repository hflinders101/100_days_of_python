import random

print("I'm thinking of a number between 1 and 100\n")
number = random.randint(1,100)
# print(number)
difficulty = input('Choose a difficulty "easy" or "hard: ').lower()
attempts = 5
if difficulty == 'easy':
	attempts = 10

def check_guess(attempts, number):
	guess = int(input('What number do you want to guess? '))
	if number > guess:
		print(f'{guess} is too low. You have {attempts - 1} left.')
		return attempts - 1, False
	elif number < guess:
		print(f'{guess} is too high. You have {attempts - 1} left.')
		return attempts - 1, False
	elif number == guess:
		print(f'Congrats, you win! The answer was {number}')
		return 0 , True


guessed_correctly = False
while not guessed_correctly:
	if attempts == 0:
		print(f'You lose! The number was {number}')
		guessed_correctly = True
		continue
	attempts, guessed_correctly = check_guess(attempts,number)
