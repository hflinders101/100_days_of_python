import turtle as t
import random

screen = t.Screen()
screen_width = 500
screen_height = 400
screen.setup(width=screen_width,height=screen_width)#This makes it easier to see when written like this
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_line = int(-screen_width/2+20)
starting_position = int(-screen_height/6*3+screen_height/12)
turtle_list = {}

for color in colors:
    racer = t.Turtle(shape='turtle')
    racer.color(color)
    racer.penup()
    racer.goto(starting_line,starting_position)
    starting_position += int(screen_height/6)
    turtle_list[color] = racer
is_race_on = False
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        rand_distance = random.randint(0,10)
        turtle_list[turtle].forward(rand_distance)
        if turtle_list[turtle].position()[0] > screen_width/2-20:
            print(f'The {turtle} turtle won the race!')
            is_race_on = False
            if user_bet == turtle:
                print(f'Since your bet on {turtle} turtle won. You bet correctly.')
            else:
                print(f'Your bet on {user_bet}, was incorrect.')


screen.exitonclick()