questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Pune", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["HTML", "Python", "C++", "All of these"],
        "answer": "All of these"
    },
    {
        "question": "What is 10 + 5?",
        "options": ["10", "15", "20", "25"],
        "answer": "15"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "bool", "float"],
        "answer": "bool"
    }
]

score = 0

print("================================")
print("       QUIZ GENERATOR 🎯")
print("================================")

for number, q in enumerate(questions, 1):

    print(f"\nQuestion {number}: {q['question']}")

    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")

    choice = int(input("Enter your answer (1-4): "))

    if q["options"][choice - 1] == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")

print("\n================================")
print("             RESULT")
print("================================")

print(f"Your score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage >= 80:
    print("🏆 Excellent!")
elif percentage >= 50:
    print("👍 Good job!")
else:
    print("📚 Keep practicing!")