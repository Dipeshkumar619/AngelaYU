from turtle import Turtle,Screen

oturtle=Turtle()
screen=Screen()
screen.exitonclick()
screen.listen()

def move_forward():
    oturtle.forward(20)

def turn_right():
    oturtle.right(90)

def turn_left():
    oturtle.left(90)

def move_backward():
    oturtle.setheading(180)
    oturtle.forward(20)
    oturtle.setheading(0)

screen.onkey('KP_Down',move_backward)
screen.onkey(KP_Left,turn_left)
screen.onkey(KP_Right,turn_right)
screen.onkey(KP_Up,move_forward)

