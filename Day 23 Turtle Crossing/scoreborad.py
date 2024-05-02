from turtle import Turtle

FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('black')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(self.score, align='center', font=FONT)

    def lose(self):
        self.goto(0,0)
        self.write(f'your final score is: {self.score}', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()