from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.penup()
        self.color('blue')
        self.shape('turtle')
        self.setheading(90)
        self.goto(0,-280)

    def player_forward(self):
        self.forward(20)



