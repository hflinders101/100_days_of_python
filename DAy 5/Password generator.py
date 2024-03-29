# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
		   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
		   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# ---------------- my code
# p_list = []
# for l in range(0,nr_letters):
#     rand_letter = random.randint(0,len(letters)-1)
#     p_list.append(letters[rand_letter])
#
# for s in range(0,nr_symbols):
#     rand_symbol = random.randint(0,len(symbols)-1)
#     p_list.append(symbols[rand_symbol])
#
# for n in range(0,nr_numbers):
#     rand_number = random.randint(0,len(numbers)-1)
#     p_list.append(numbers[rand_number])
#
# new_pass = random.sample(p_list,len(p_list))
#
# print("A good password would be:")
# print("".join(new_pass))

# Alt option they created
password_list = []
for char in range(1, nr_letters + 1):
	password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
	password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
	password_list += random.choice(numbers)
random.shuffle(password_list)

password = ""
for char in password_list:
	password += char
print(f'Your password is: {password}')
