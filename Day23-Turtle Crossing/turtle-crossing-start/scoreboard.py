from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.create_score()

    def create_score(self):
        self.goto(-280,260)
        self.color("black")
        self.hideturtle()
        self.write(f"Level: {self.level}",align="left",font=FONT)


    def update_score(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over !!",align="center",font=FONT)











