import turtle as t # Typically you should use this so the reader can understand your code
from random import randint
import random

from turtle import Turtle #Only use this if using it more than 3 times

tim = t.Turtle()
tim.shape('turtle')
tim.color('DodgerBlue')
shapes = {
    'triangle': [3, 'red'],
    'square': [4, 'blue'],
    'pentagon': [5, 'green'],
    'hexagon': [6, 'purple'],
    'octagon': [8, 'orange'],
    'nonagon': [9, 'yellow'],
    'decagon': [10, 'red'],
}
# print(type(shapes['triangle'][0]))
# for shape in shapes:
#     sides = shapes[shape][0]
#     tim.color(shapes[shape][1])
#     for i in range(1,sides+1):
#         tim.forward(100)
#         tim.right(360/sides)
#---------------------------------My answer above, hers below ------------

t.colormode(255)
# def draw_shape(n_sides):
#     angle = 360/n_sides
#     for _ in range(n_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3,11):
#     r = randint(0,255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     tim.color(r,b,g)
#     draw_shape(shape_side_n)

#--------- Random walk -----------
# tim.pensize(10)
tim.speed(0)
# step_size = 30
# movement_list = [0,90,180,270]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r,g,b)
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(step_size)
#     tim.setheading(random.choice(movement_list))
#---------------------------- spirograph below ----------
def draw_spirograph(size_of_gap):
    for degree in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        heading = tim.heading()
        tim.setheading(heading + size_of_gap)

# draw_spirograph(69)














screen = t.Screen()
screen.exitonclick()