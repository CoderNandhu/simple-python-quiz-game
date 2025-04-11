score = 0

questions = [
    {
        "question": "What is the real name of the actor in the movie Iron Man?",
        "options": ["A. Tony Stark", "B. Mohammad Ali", "C. Robert Downey Jr."],
        "answer": "C"
    },
    {
        "question": "What is CPU?",
        "options": ["A. Control Pocket Unit", "B. Central Processing Unit", "C. Cover Protection Unit"],
        "answer": "B"
    },
    {
        "question": "Who is the developer of Facebook?",
        "options": ["A. Mark Zuckerberg", "B. Stan Lee", "C. Bill Gates"],
        "answer": "A"
    }
]

print(type(questions))

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    answer = input("Enter your choice A,B,C \n").upper()

    if answer == q["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print("Oops! That's not right. 😢")

print(f"Your Final score is {score} !!!!")

# for option in question1["options"]:
#     print(option)

# user_answer = input("Enter your choice \n").upper()

# if user_answer == question1["answer"]:
#     print("Correct! 🎉")
# else:
#     print("Oops! That's not right. 😢")
