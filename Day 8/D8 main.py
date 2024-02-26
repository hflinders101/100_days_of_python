# # Write your code below this line 👇
# def paint_calc(height,width,cover):
#   cans = round(height*width/cover+.4)
#   return print(f"You'll need {cans} cans of paint.")
# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.
# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
# #-------------------------------------

# Write your code below this line 👇
def prime_checker(number):
	# mod_val = []
	# decision = 0
	# if number > 9:
	# 	for val in range(2,10):
	# 		mod_val.append(number % val)
	# 	if not 0 in mod_val:
	# 		decision = "It's a prime number."
	# 	else:
	# 		decision = "It's not a prime number."
	# elif number == 2 or number ==3 or number ==5 or number == 7:
	# 	decision = "It's a prime number."
	# elif number == 1 or number == 4 or number == 6 or number == 8 or number ==9:
	# 	decision = "It's not a prime number."
	##-------------- code they wrote
	is_prime = True
	for n in range(2,number):
		value = number % n
		if value == 0:
			is_prime = False
	if is_prime:
		print("It's a prime number.")
	else:
		print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)