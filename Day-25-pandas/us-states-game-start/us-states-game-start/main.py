import turtle

import pandas

screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
score=0
attempt=0
turtle.shape(image)
data=pandas.read_csv('50_states.csv')
all_states=data['state'].to_list()
is_game_on=True
while is_game_on and attempt <= len(all_states):
    answer = screen.textinput(title="Guess the state", prompt="What's the another state's name ")
    attempt += 1
    if answer in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())
        t.write(answer)
        score += 1
    if answer != "exit":
        screen.title(f"{score}/{attempt}")
        continue
    break

screen.exitonclick()