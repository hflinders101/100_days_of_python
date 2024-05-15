import turtle
from turtle import Screen
from player import Player
import time
from car import Car
from scoreborad import Scoreboard


screen = Screen()
screen_width = 600
screen_height = 600
screen.setup(width=screen_width, height=screen_height)
screen.title('Turtle Crossing')
screen.tracer(0)
turtle.colormode(255)

player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.player_forward, 'Up') #can't have () after the function

starting_cars = 10
list_of_cars = []
car_positions = []
speed_of_cars = .3

for vehicle in range(0,starting_cars):
    car = Car()
    car.start_random()
    car.check_next_to_another_car(list_of_cars)
    list_of_cars.append(car)
    screen.update()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(car.car_speed)
    for vehicle in list_of_cars:
        vehicle.move_forward()
        if vehicle.xcor() < -screen_width/2 - 40:
            list_of_cars.remove(vehicle)
        if player.distance(vehicle) < 22:
            print('game over')
            scoreboard.lose()
            game_is_on = False

    if player.ycor() >= 280:
        scoreboard.increase_score()
        player.create_player()
        car.increase_speed()

    car = Car()
    car.start_at_edge()
    car.check_next_to_another_car(list_of_cars)
    list_of_cars.append(car)


screen.exitonclick()