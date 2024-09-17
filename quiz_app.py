def ask_question(question, options, correct_option):
    print(question)
    for option in options:
        print(option)
    
    answer = int(input("Choose the correct option (1-4): "))
    
    if answer == correct_option:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer was: {options[correct_option - 1]}\n")
        return 0

def quiz():
    score = 0
    questions = [
        {
            "question": "What does HTML stand for?",
            "options": ["1. HyperText Markup Language", "2. Hyperlinks and Text Markup Language", 
                        "3. Home Tool Markup Language", "4. Hyper Tool Markup Language"],
            "correct_option": 1
        },
        {
            "question": "Which HTML tag is used to define an unordered list?",
            "options": ["1. <ul>", "2. <ol>", "3. <li>", "4. <list>"],
            "correct_option": 1
        },
        {
            "question": "Which CSS property is used to change the background color?",
            "options": ["1. color", "2. background-color", "3. bgcolor", "4. background"],
            "correct_option": 2
        },
        {
            "question": "What does CSS stand for?",
            "options": ["1. Cascading Style Sheets", "2. Colorful Style Sheets", 
                        "3. Computer Style Sheets", "4. Creative Style Sheets"],
            "correct_option": 1
        },
        {
            "question": "Which of the following is a TypeScript data type?",
            "options": ["1. string", "2. number", "3. boolean", "4. All of the above"],
            "correct_option": 4
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["1. def", "2. func", "3. function", "4. lambda"],
            "correct_option": 1
        },
        {
            "question": "How do you insert comments in Python code?",
            "options": ["1. // comment", "2. # comment", "3. <!-- comment -->", "4. /* comment */"],
            "correct_option": 2
        },
        {
            "question": "Which of the following is used to style websites?",
            "options": ["1. HTML", "2. CSS", "3. Python", "4. SQL"],
            "correct_option": 2
        },
        {
            "question": "What is the correct syntax for referring to an external script called 'app.js' in HTML?",
            "options": ["1. <script href='app.js'>", "2. <script name='app.js'>", 
                        "3. <script src='app.js'>", "4. <script link='app.js'>"],
            "correct_option": 3
        },
        {
            "question": "Which of the following is a valid way to declare a variable in TypeScript?",
            "options": ["1. var myVar", "2. let myVar", "3. const myVar", "4. All of the above"],
            "correct_option": 4
        }
    ]
    
    for q in questions:
        result = ask_question(q["question"], q["options"], q["correct_option"])
        if result == 0:
            break
        score += result
    
    print(f"Your final score is: {score}")

quiz()
