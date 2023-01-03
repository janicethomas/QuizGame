from quizBrain import quizBrain
from data import question_bank
from led import ledBlink

quiz = quizBrain(question_bank)
led = ledBlink()

while quiz.still_has_questions():
    quiz.next_question()

print('Score: '+ str(quiz.score))
led.score_blink(quiz.score)
