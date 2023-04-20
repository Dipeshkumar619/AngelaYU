from turtle import Screen
import time
from snake import  Snake
from food import Food
from scoreboard import Scoreboard
from food import Food
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=Scoreboard()
game_is_on=True
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
#     Detec Snake Collions with food
    if snake.head.distance(food) < 15:
        print("nom nom nom ")
        score.update_score()
        snake.extend_snake()
        food.refresh()
    #     Detec Snake Collions with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("I am into walls !!")
        game_is_on=False
        score.game_over()
    #     Detec Snake Collions with tail
    for body in snake.all_turtles[1:]:
        if snake.head.distance(body) < 5:
            print("Ohh !! eaten my Lovely tail")
            game_is_on=False
            score.game_over()






screen.exitonclick()