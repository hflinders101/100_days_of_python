from menu import *

resources = {"Water": 300,
			 "Milk": 200,
			 'Coffee': 100,
			 'Money': 0
}
def take_money(order, resources_dict, menu):
	"""Asks user for money input, returns amount of money"""
	print('Put the number of coins you have in')
	quarters = int(input('Quarters: '))
	dimes = int(input('Dimes: '))
	nickels = int(input('Nickels: '))
	pennies = int(input('Pennies: '))
	money_recieved = round(quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01,2)
	menu_cost = menu[order]['cost']
	change = round(money_recieved - menu_cost, 2)

	if money_recieved < menu_cost:
		print(f"${resources_dict['Money']} isn't enough to afford a {order}. Here is your ${resources_dict['Money']} back.")
	else:
		resources_dict['Money'] -= change
		print(f'Thank you for purchasing a {order}, your change is ${change}')

def check_resources(order, resources_dict, menu):
	menu_water = menu[order]['ingredients']['water']
	menu_coffee = menu[order]['ingredients']['coffee']
	menu_milk = menu[order]['ingredients']['milk']
	if resources_dict['Water'] >= menu_water and resources_dict['Coffee'] >= menu_coffee\
			and resources_dict['Milk'] >= menu_milk:
		resources_dict['Water'] -= menu_water
		resources_dict['Coffee'] -= menu_coffee
		resources_dict['Milk'] -= menu_milk
	elif resources_dict['Water'] < menu_water or resources_dict['Coffee'] < menu_coffee\
			or resources_dict['Money'] < menu_cost or resources_dict['Milk'] < menu_milk:
		for ingredients in menu[order]['ingredients']:
			rescources_key = ingredients.capitalize()
			if resources_dict[rescources_key] < menu[order]['ingredients'][ingredients]:
				print(f"There isn't enough {ingredients} in the machine")
		return True
	return False
def print_resources(resources_dict):
	print('Here is a report of the machine reources')
	water = resources_dict['Water']
	coffee = resources_dict['Coffee']
	money = resources_dict['Money']
	milk = resources_dict['Milk']
	print(f'Water: {water}mL')
	print(f'Milk: {milk}mL')
	print(f'Coffee: {coffee}g')
	print(f'Money: ${money}')



turn_off = False
not_enough = False
while not turn_off:
	order = input('What kind of drink would you like? Espresso ($1.5), latte ($2.5), or cappuccino ($3)?').lower()
	not_enough = check_resources(order, resources, MENU)
	if not_enough == False:
		take_money(order, resources, MENU)
		keep_going = input('Do you want to order again? y/n: ').lower()
		if keep_going == 'n':
			turn_off = True
	else:
		turn_off = True

