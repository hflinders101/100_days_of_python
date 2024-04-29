# from turtle import *
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import *

table = PrettyTable()
table.field_names = ['Pokemon Name', 'Type']
table.add_rows(
	[
		["Pikachu", 'Electric'],
		['Squirtle', 'Water'],
		['Charmander', 'Fire']
	]
)
print(table.align)
table.align = 'l'

print(table)
