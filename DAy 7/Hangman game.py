# Step 4

import random
import hangman_art
from words import word_list
from replit import clear

end_of_game = False
word_list = word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guessed_letters = []
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
	display += "_"
print(hangman_art.logo)
print(hangman_art.stages[6])
while not end_of_game:
	guess = input("Guess a letter: ").lower()
	clear()
	if guess in display or guess in guessed_letters:
		print(f'You have already guessed {guess}. Please try again.')

	# Check guessed letter
	for position in range(word_length):
		letter = chosen_word[position]
		# print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
		if letter == guess:
			display[position] = letter


	if guess not in chosen_word and guess not in guessed_letters:
		lives -= 1
		guessed_letters.append(guess)
		print(hangman_art.stages[lives])
		print(f'The letter {guess} is not in the word. You lose a life and have {lives} tries left.')
	# Then reduce 'lives' by 1.
	# If lives goes down to 0 then the game should stop and it should print "You lose."

	# Join all the elements in the list and turn it into a String.
	print(f"{' '.join(display)}")

	# Check if user has got all letters.
	if "_" not in display:
		end_of_game = True
		print("You win.")
	elif lives == 0:
		end_of_game = True
		print(f'You lose. The word was: {chosen_word}')