import time
from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)

    def refresh(self):
        random_x=random.randint(-270,270)
        random_y=random.randint(-270,270)
        self.goto(random_x,random_y)

    def glowing(self):
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        time.sleep(0.1)
        self.shapesize(stretch_len=1,stretch_wid=1)
        time.sleep(0.1)










