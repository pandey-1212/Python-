# Python quiz game

question = ("How many element are in the periodic table:",
           "Which animal lays the largest eggs:",
           "What is the most abundant gas in Earth's atmosphere:",
           "How many bones are in the human body:",
           "Which planet in the solar system is the hottest:")

options = (("A. 116", "B. 117", "C. 118", "D. 119")
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich")
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen")
           ("A. 205", "B. 209", "C. 206", "D. 308")
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

 answers = ("C", "D", "A", "C", "B") 
 guesses = []
 score = 0
 question_num = 0

 for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]
        print(option)
      
     guess = input("Enter (A, B, C, D):").upper()
     guesses.append(guess)
     if guess == answer[question_num]:
        score +=1
        print("CORRECT!")
     else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")   
     question_num += 1        

                  