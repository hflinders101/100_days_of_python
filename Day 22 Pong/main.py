from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

winning_score = 5

screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
speed_increaser = 0

screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    screen.update()  # use this for loop to keep updating the screen so it doesn't need to be in the class. This goes
    # with the tracer
    time.sleep(ball.ball_Speed)
    ball.move()
    position = ball.position()[1]
    if abs(ball.ycor()) > (screen_height/2-10):
        ball.bounce_y()

    #Detect colission with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        speed_increaser += .005

    #detect is paddle misses
    elif abs(ball.xcor()) > 325:
        if ball.xcor() > 0:
            scoreboard.l_point()
        else:
            scoreboard.r_point()
        ball.reset_ball()

    scoreboard.check_if_won(winning_score)
    if scoreboard.l_score == winning_score or scoreboard.r_score == winning_score:
        game_is_on = False


screen.exitonclick()
