import random

#--------------------------
# heads or tails generator
# flip = random.randint(0,1)
# if flip == 1:
#     print(f"Heads")
# else: print("Tails")
#--------------------------
#--------------------------
#Banker roulette
# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# buyer = names[random.randint(0,len(names)-1)]
# print(f'{buyer} is going to buy the meal today!')
#--------------------------
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?⬜️
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# position = position.lower()
# if "a" in position:
#     letter = 0
# elif "b" in position:
#     letter = 1
# else:
#     letter = 2
# if "1" in position:
#     num = 0
# elif "2" in position:
#     num = 1
# else:
#     num = 2
# map[num][letter] = "X"

# #---- this is what she did. She used indexes
# letter = position[0].lower()
# abc = ['a','b','c']
# letter_index = abc.index(letter)
# number_index = int(position[1])-1
# map[number_index][letter_index] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")