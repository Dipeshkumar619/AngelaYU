from turtle import Turtle,Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore=0
        self.lscore=0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,240)
        self.write(f"{self.lscore} | {self.rscore}",align="center",font=("Courier",40,"normal"))

    def update_rscore(self):
        self.rscore+=1
        self.clear()
        self.write(f"{self.lscore} | {self.rscore}",align="center",font=("Courier",40,"normal"))

    def update_lscore(self):
        self.lscore+=1
        self.clear()
        self.write(f"{self.lscore} ||  {self.rscore}",align="center",font=("Arial",24,"normal"))