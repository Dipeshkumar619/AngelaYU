import turtle as t
from turtle import Screen
import random
screen = Screen()
screen.colormode(255)

tim=t.Turtle()
# Screen=tim.screen()
# colors=["dark slate blue","slate blue","medium blue","light blue","dim gray","slate gray","dark slate gray","teal","dark cyan","yellow","magenta","light pink","dodger blue","cadet blue","violet red"]
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
directions = [ 0,45,90, 180, 270]
tim.speed("fastest")
while True:
    tim.pensize(15)
    tim.color(random_color())
    tim.right(random.choice(directions))
    tim.forward(30)