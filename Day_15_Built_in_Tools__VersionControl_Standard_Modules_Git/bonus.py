from email import message
import json
from unittest import result

with open("questions.json","r") as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_test"])
    for index, alternive in enumerate(question["alternatives"]):
        print(index +1, "-" ,alternive)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score =  score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = f"{result} {index + 1} - Your Answer: {question['user_choice']}, " \
              f"Correct Answer: {question['correct_answer']}"
    
    print(message)


print(score, "/", len(data))
