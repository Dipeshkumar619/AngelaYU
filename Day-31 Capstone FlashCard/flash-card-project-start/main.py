import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from pandas import *

def flip_card():
    canvas.itemconfig(frontcanvas,image=cardBackimage)
    canvas.itemconfig(frenchtitle,text="English",fill="white")
    canvas.itemconfig(title,text=f"{answer}",fill="white")

window=Tk()
window.title("Flash Card Game!!")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_func=window.after(3000,func=flip_card)
canvas=Canvas(height=526,width=800)

df=pandas.read_csv("data\\french_words.csv")
french=df.to_dict(orient="records")


def generate_newword():
    Quest = random.choice(french)
    global Question,answer,flip_func
    Question = Quest["French"]
    answer = Quest["English"]
    canvas.itemconfig(frenchtitle,text="French",fill="black")
    canvas.itemconfig(frontcanvas, image=cardFrontimage)
    canvas.itemconfig(title,text=f"{Question}",fill="black")
    saving_csv()
    # time.sleep(3)

def saving_csv():
    print(len(french))
    french.remove(Quest)
    generate_newword()

rightimage=PhotoImage(file="images\\right.png")
wrongimage=PhotoImage(file="images\\wrong.png")
rightButton=Button(image=rightimage,highlightthickness=0,command=generate_newword)
rightButton.grid(row=1,column=1)
cardFrontimage=PhotoImage(file="images\\card_front.png")
cardBackimage=PhotoImage(file="images\\card_back.png")

frontcanvas=canvas.create_image(400,263,image=cardFrontimage)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
frenchtitle=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
title=canvas.create_text(400,263,text="Title",font=("Arial",60,"bold"))

wrongButton=Button(image=wrongimage,highlightthickness=0,command=flip_card)
wrongButton.grid(row=1,column=0)


generate_newword()
canvas.grid(row=0,column=0,columnspan=2)
window.mainloop()

