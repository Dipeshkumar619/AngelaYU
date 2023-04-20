from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.xmove=10
        self.ymove=10
        self.speed("fastest")
        self.move_speed=0.1

    def move(self):
        self.penup()
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.ymove *=-1

    def bounce_x(self):
        self.xmove*=-1
        self.move_speed*=0.9

    def detect_wallcollision(self):
        if self.ycor() > 280  or self.ycor() < -280:
            print("Collision detected on walls")
            self.bounce_y()

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()
