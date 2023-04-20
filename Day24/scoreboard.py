from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial,24,normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)


    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("yellow")
        self.write(f"Game Over !!",align="center",font=("Arial",24,"normal"))




