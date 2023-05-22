THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface():
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizier")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        falseImage=PhotoImage(file="images/false.png")
        trueImage=PhotoImage(file="images/true.png")
        self.falseButton=Button(image=falseImage,highlightthickness=0,command=self.wrong_func)
        self.trueButton=Button(image=trueImage,highlightthickness=0,command=self.right_func)
        self.canvas=Canvas(height=400,width=300,bg=THEME_COLOR)
        self.question_text=self.canvas.create_text(150,125,width=280,text="Question Text",font=("Arial",15,"italic"))
        self.falseButton.grid(row=2,column=0)
        self.trueButton.grid(row=2,column=1)
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=2,columnspan=2)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.get_nextquestion()
        self.window.mainloop()

    def get_nextquestion(self):
        self.canvas.config(bg=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.canvas.config(bg=THEME_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You Have reached the end of the questions!!")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")



    def wrong_func(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def right_func(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_nextquestion)





