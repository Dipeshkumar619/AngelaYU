from tkinter import  *
import  math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
timer_status="Timer"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
        global reps
        global timer_status
        reps+=1
        print(reps)
        if reps==8:
            count_down(60*LONG_BREAK_MIN)
            timer_status="Long Break"
            title.config(text=f"{timer_status}",fg=RED)
            reps=0
        elif reps%2==0:
            count_down(60*SHORT_BREAK_MIN)
            timer_status="Short Break"
            title.config(text=f"{timer_status}",fg=PINK)

        else:
            count_down(WORK_MIN*60)
            timer_status="Work"
            title.config(text=f"{timer_status}",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# import time
# time.sleep(1)
# count=5
# while True:
#     time.sleep(1)
#     count-=1

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import  *
import time
window=Tk()
window.title("Pomodoro")

window.config(pady=10,padx=10,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
title=Label(text=f"{timer_status}",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
title.grid(column=1,row=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    if count_min < 10:
        count_min=f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
            check_mark.config(text=mark)
# def count_down(count):
#     canvas.itemconfig(timer_text,text=count)
#     print(count)
#     if count >1:
#         window.after(1000,count_down,count-1)
start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark=Label(highlightthickness=0,fg=GREEN)
check_mark.grid(column=1,row=3)


# calculate_button.grid(column=2,row=0)

canvas.grid(column=1,row=1)
window.mainloop()