import random

question=[
    {
        "question":"What is the capital of India?",
        "answer":"new delhi"
    },
    {
        "question":"What are we learning right now",
        "answer":"python"
    },
    {
        "question":"how many days in a week?",
        "answer":"7"
    },
    {
        "question":"how many months in a year?",
        "answer":"12"
    }
]

def start_quiz():
    random_question=random.choice(question)
    print("YOUR QUIZ")
    print(random_question["question"])
    user_answer=input("Enter your Answer:").lower()
    if user_answer==random_question["answer"]:
        print("Correct Answer")
    else:
        print("Wrong Answer")
        print(random_question["answer"])