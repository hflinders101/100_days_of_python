from Data import *
from random import *
# print(type(data[1]['follower_count']))
#Pick names and people to compare
#get name picker function, don't let same thing be picked twice ever
#See which one has more followers on twitter
# get point if guess correctly
list_of_picks = []
points = 0
def comp_guess_pick(list_of_picks):
	random_number = randint(0,len(data))
	if list_of_picks in list_of_picks:
		comp_guess_pick()
	else:
		list_of_picks.append(random_number)
		return random_number
keep_going = True
comp_guess_1_index = comp_guess_pick(list_of_picks)
while keep_going:
	comp_guess_2_index = comp_guess_pick(list_of_picks)

	# print(f"guess 1 is: {data[comp_guess_1_index]['follower_count']}")
	# print(f"guess 2 is: {data[comp_guess_2_index]['follower_count']}")

	if data[comp_guess_1_index]['follower_count'] > data[comp_guess_2_index]['follower_count']:
		winner = 1
	else:
		winner = 2
	user_guess = input(f'Does {data[comp_guess_1_index-1]["name"]} have a higher or lower amount of followers than {data[comp_guess_2_index-1]["name"]}? ').lower()

	if (user_guess == 'higher' and winner == 1) or (user_guess == 'lower' and winner == 2):
		comp_guess_1_index = comp_guess_2_index
		points += 1
		print(f'You have {points} points')
	else:
		print(f'You lose with a score of {points}')
		keep_going = False



