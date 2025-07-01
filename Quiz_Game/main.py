from model import Question
from data import question_data
from quizbrain import QuizBrain

question_bank=[]
for q_no in question_data:
    qns=Question(q_no["question"],q_no["correct_answer"])
    question_bank.append(qns)

work=QuizBrain(question_bank)
while work.still_has_questions():
    work.next_question()
print("WELL DONE! You've completed the quiz greatly!")
print(f"Your final score is {work.score} out of {len(question_bank)}")
