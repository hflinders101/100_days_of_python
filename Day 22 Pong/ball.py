from turtle import Turtle
import random



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.ball_Speed = .1

    def create_ball(self):
        self.penup()
        self.shape('circle')
        self.color('white')
        self.goto(0,0)
        # rand_heading = random.randint(0,360)
        # while 80 < rand_heading < 130 or 230 < rand_heading < 310:
        #     rand_heading = random.randint(0,360)
        # self.setheading(rand_heading)

    def move(self):
        # self.forward(5)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        # heading_angle = self.heading()
        # if heading_angle < 90:
        #     self.setheading(heading_angle - 90)
        #     self.move()
        # elif heading_angle < 180:
        #     self.setheading(heading_angle + 90)
        # elif heading_angle < 270:
        #     self.setheading(heading_angle - 90)
        # elif heading_angle < 360:
        #     self.setheading(heading_angle + 90)
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.ball_Speed *= .9

    def reset_ball(self):
        self.create_ball()
        self.bounce_x()
        self.ball_Speed = .1





