
#functions for basic calulator stuff
def add(a,b):
	return a + b
def subtract(a,b):
	return a - b
def multiply(a,b):
	return a * b
def divide(a,b):
	return a / b

operations={
	'+': add,
	'-': subtract,
	'*': multiply,
	'/':  divide,
}
def calculator():
	keep_going = True
	while keep_going is True:
		counter = 0
		if counter < 1:
			num1 = float(input('what is the first number?: '))
			for operator in operations:
				print(operator)
			operation_symbol = input('pick a symbol from the line above: ')

			num2 = float(input('what is the second number?: '))

			first_answer = operations[operation_symbol](num1,num2)
			print(f'{num1} {operation_symbol} {num2} = {first_answer}')
			counter += 1
			keep_going = input(f'type "y" to continue with {first_answer}, or type "n" to start a new calculation: ').lower()
		if keep_going == 'y':
			operation_symbol = input('pick a symbol: ')
			num3 = float(input('pick another number: '))
			calculator_function = operations[operation_symbol]
			second_answer = calculator_function(first_answer,num3)
			print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')
			first_answer = second_answer
			keep_going = input(f'type "y" to continue with {first_answer}, or type "n" to start a new calculation: ').lower()
		if keep_going == 'y':
			keep_going = True
		else:
			keep_going = False
			calculator() #This is the idea of recursion. Make sure to have conditions so it's not infinite
calculator()



