questions=[
    {
        "prompt": "What is the capital of France",
        "options": ["A.Paris", "B.London", "C.Berlin", "D.Madrid"],
        "answer": "A"
    
    },
    {
        "prompt":"Which language is spoken in Brazil",
        "options": ["A.Spanish", "B.Portuguese", "C.English", "D.French"],
        "answer": "B"
    },
    {
        "prompt": "Where is Marine drives located",
        "options": ["A.Mumbai", "B.Delhi", "C. Nashik", "D.Pune"],
        "answer": "A"
    },
    {
        "prompt": "Who wrote Jana Gana Mana",
        "options": ["A.Varun Dhawan", "B.Shradha Kapoor", "C.Rabindranath Tagore", "D.Bankim Chandra Chaterjee "],
        "answer":"C"
    }
]

def quizz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
            
        user_answer=input("Enter your Answer:")
        if user_answer.upper()==question["answer"]:
            

            print(f"Correct Answer!!!{question['answer']}\n")
            score+=1
        else:
            
            print(f"Oh NOOO the correct answer is {question['answer']}")
    print(f"You got{score} out of {len(questions)} questions correct ") 



