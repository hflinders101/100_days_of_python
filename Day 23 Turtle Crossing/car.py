from turtle import Turtle
import random

X_BOUND = 240
Y_BOUND = 240
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.random_color()
        self.car_speed = .3
        self.make_car()


    def random_color(self):
        color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40),
                      (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159),
                      (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102),
                      (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39),
                      (164, 209, 187), (151, 206, 220)]
        self.color(random.choice(color_list))

    def make_car(self):
        self.penup()
        self.shape('square')
        car_size = random.randint(1,3)
        self.shapesize(stretch_len=car_size)

    def faster_car(self):
        self.car_speed *= 1.5

    def start_at_edge(self):
        random_y_cord = random.randint(-Y_BOUND,Y_BOUND)
        self.goto(300,random_y_cord )
    def start_random(self):
        random_y_cord = random.randint(-Y_BOUND, Y_BOUND)
        random_x_cord = random.randint(-X_BOUND, X_BOUND)
        self.goto(random_x_cord, random_y_cord)

    def move_forward(self):
        self.setheading(180)
        self.forward(20)

    def check_next_to_another_car(self,list_of_cars):
        next_to_another_car = True
        min_distance = 40
        while next_to_another_car:
            next_to_another_car = False  # Assume the turtle isn't next to another car
            for car in list_of_cars:
                if car.distance(self) < min_distance:
                    next_to_another_car = True
                    self.start_at_edge()  # Restart the random placement process
                    break

    def increase_speed(self):
        self.car_speed *= .9
