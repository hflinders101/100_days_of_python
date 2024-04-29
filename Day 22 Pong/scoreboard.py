from turtle import Turtle

FONT = ('Courier', 80, 'normal')
WINNING_FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=FONT)
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def check_if_won(self, winning_score):
        self.goto(0, 0)
        if self.l_score == winning_score:
            self.write('Left side won!', align='center', font=WINNING_FONT)
        elif self.r_score == winning_score:
            self.write('Right side won!', align='center', font=WINNING_FONT)

