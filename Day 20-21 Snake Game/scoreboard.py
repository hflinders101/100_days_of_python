from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 22, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)
