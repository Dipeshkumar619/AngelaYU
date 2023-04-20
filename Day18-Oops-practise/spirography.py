from turtle import Turtle,Screen
import random
oturtle=Turtle()
oturtle.pensize(4)
oturtle.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

def draw_circles(gapsize):
        for _ in range(int(360/gapsize)):
            oturtle.color(random_color())
            oturtle.circle(50)
            oturtle.setheading(oturtle.heading()+gapsize)

screen=Screen()
screen.colormode(255)

draw_circles(4)

screen.exitonclick()
