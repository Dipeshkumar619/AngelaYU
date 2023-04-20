from turtle import Turtle,Screen
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_position=[(0,0),(-20,0),(-40,0)]
screen.tracer(0)

all_turtle=[]
for position in starting_position:
    turtle = Turtle("square")
    turtle.penup()
    turtle.color("white")
    turtle.goto(position)
    all_turtle.append(turtle)

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.2)

    for seg_num in range(len(all_turtle)-1,0,-1):
        new_x=all_turtle[seg_num-1].xcor()
        new_y=all_turtle[seg_num-1].ycor()
        all_turtle[seg_num].goto(new_x,new_y)
    all_turtle[0].forward(10)
    all_turtle[0].left(90)






screen.exitonclick()
