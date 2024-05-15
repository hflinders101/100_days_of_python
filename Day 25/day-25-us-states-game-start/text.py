from turtle import Turtle

FONT = ('Courier', 8, 'normal')
FONT_WIN = ('Courier', 80, 'normal')
class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()

    def write_text(self, x_cor, y_cor, state_name):
        self.goto(x= x_cor, y= y_cor)
        # self.pendown()
        self.write(state_name, align='center', font=FONT)

    def winning_text(self):
        self.goto(0,0)
        self.clear()
        self.write('You won!!!', align='center', font=FONT_WIN)

