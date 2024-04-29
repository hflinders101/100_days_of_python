#must use 100_days_of_python environment for this
import colorgram
import turtle as t
import random
###########inptus##########
photo_file_path = r'C:\Users\hflin\PycharmProjects\100_days_of_python\Day 18 Turtle and the GUI\hirstpainting.jpg'
spacing = 20
grid_size = 10
dot_size = 20
########## end inputs##########
def colors_from_colorgram(photo_file_path, n_of_colors_you_want):
    """Takes in a filepath for a jpg, outputs a list with rgb tuples. The n_of_colors_you_want is how many color tuples will be
    in your list output."""
    colorgram_list = colorgram.extract(photo_file_path, n_of_colors_you_want)
    my_colors_list = []
    for color in colorgram_list:
        r= color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_tuple = (r,g,b)
        my_colors_list.append(new_tuple)
    return my_colors_list

# # colors_list = colors_from_colorgram(photo_file_path,30) #Need to take out colors close to 255
# print(colors_list)
# color_list = colors_from_colorgram(photo_file_path,30)
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.pensize(20)
tim.penup()
tim.hideturtle()

for y in range(int(-grid_size/2), int(grid_size/2)):
    for x in range(int(-grid_size / 2), int(grid_size / 2)):
        tim.color(random.choice(color_list))
        tim.setposition(x*spacing,y*spacing)
        tim.dot(dot_size)
screen = t.Screen()
screen.exitonclick()

