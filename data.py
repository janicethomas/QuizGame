import requests

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

parameters = {
    "amount": 5,
    "type": "boolean",
    "category": 12
}

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params = parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
# print(question_data)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
