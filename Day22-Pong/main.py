from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong Game")
screen.tracer(0)
right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball=Ball()
score=Score()
is_game_on=True
screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    ball.detect_wallcollision()
    # if ball.distance(right_paddle) or ball.distance(left_paddle) < 21:
    #     print("paddle bounce detected !!")
    #     ball.paddle_bounce()
#     Detect Right paddle connect with ball
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()
#    Right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_lscore()
    elif ball.xcor() < -380:
        ball.reset_position()
        score.update_rscore()

screen.exitonclick()