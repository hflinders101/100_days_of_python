from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,coordintate_tuple):
        super().__init__()
        self.cord = coordintate_tuple
        self.paddle_sizing()

    def paddle_sizing(self):
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=(100 / 20))
        self.setheading(90)
        self.goto(self.cord)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
