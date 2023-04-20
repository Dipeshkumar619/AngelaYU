from turtle import Turtle,Screen
import time

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.all_turtles=[]
        self.create_snake()
        self.head=self.all_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_turtle(position)


    def add_turtle(self,position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.all_turtles.append(turtle)

    def move_snake(self):
            for seg_num in range(len(self.all_turtles) - 1, 0, -1):
                new_x = self.all_turtles[seg_num - 1].xcor()
                new_y = self.all_turtles[seg_num - 1].ycor()
                self.all_turtles[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend_snake(self):
        self.add_turtle(self.all_turtles[-1].position())
