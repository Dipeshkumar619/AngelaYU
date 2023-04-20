from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        # self.goto(280,0)
        self.setposition(position)

    def go_up(self):
        if self.ycor() < 230:
            new_y=self.ycor()+40
            self.goto(self.xcor(),new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y=self.ycor()-40
            self.goto(self.xcor(),new_y)