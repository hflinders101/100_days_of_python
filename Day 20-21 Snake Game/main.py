import turtle as t
import time
import snake
import food
from scoreboard import Scoreboard

screen = t.Screen()
screen_width= 600
screen_height = 600
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()