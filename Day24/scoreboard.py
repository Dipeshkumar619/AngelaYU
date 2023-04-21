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
        self.high_score()
        self.write(f"Score:{self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)


    def high_score(self):
        with open('data.txt',mode='r') as file:
            self.high_score=int(file.read())


    def update_score(self):
        self.score+=1
        self.clear()
        if self.score > self.high_score:
            self.high_score=self.score
            with open('data.txt', mode='w') as file:
                file.write(f"{self.high_score}")
        self.write(f"Score:{self.score} High Score: {self.high_score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("yellow")
        self.write(f"Game Over !!",align="center",font=("Arial",24,"normal"))




