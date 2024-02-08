import random

#--------------------------
# heads or tails generator
# flip = random.randint(0,1)
# if flip == 1:
#     print(f"Heads")
# else: print("Tails")
#--------------------------
#Banker roulette
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
buyer = names[random.randint(0,len(names)-1)]
print(f'{buyer} is going to buy the meal today!')