import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.listen()
player=Player()
car=CarManager()
level=Scoreboard()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for onecar in car.all_cars:
        if onecar.distance(player) < 20:
            level.game_over()
            game_is_on=False
        if player.ycor() > 290:
            level.update_score()
            car.increase_speed()
            player.create_player()

screen.exitonclick()



