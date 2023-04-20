from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    # print(i["text"],i["answer"])\
    question_text=i["text"]
    question_answer=i["answer"]
    new=Question(question_text,question_answer)
    question_bank.append(new)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
quiz.print_final_score()


