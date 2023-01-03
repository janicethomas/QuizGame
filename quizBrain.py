from led import ledBlink

led = ledBlink()

class quizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.score = 0
        self.question_number = 0
        self.answer = None
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        text = current_question.text
        self.answer = current_question.answer
        self.question_number += 1
        user_answer = raw_input(text + "(True/False): ")
        print("\n")
        self.check_answer(user_answer)
    
    def check_answer(self, user_answer):
        if str(user_answer.lower()) == str(self.answer.lower()):
            self.score += 1
            led.blink_green()
        else:
            led.blink_red()
