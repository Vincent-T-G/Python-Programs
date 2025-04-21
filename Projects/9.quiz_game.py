#This is python project number 9
#TITLE:QUIZ GAME

#It's a quiz program using python

questions = (
             "What is the name of the force that pulls objects towards the Earth?: ",
             "What is the process by which plants make their own food?: ",
             "What is the name of the structure in a cell that contains the genetic material (DNA)?: ",
             "Which state of matter has a definite volume but no fixed shape?: ",
             "What is the scientific term for the process of a liquid turning into a gas?: "
            )

options = (
           ("A. Friction", "B. Inertia", "C. Gravity", "D. Magnetism"),
           ("A. Respiration", "B. Photosynthesis", "C. Digestion", "D. Excretion"),
           ("A. Mitochondria", "B. Nucleus", "C. Ribosome", "D. Cytoplasm"),
           ("A. Solid", "B. Gas", "C. Liquid", "D. Plasma"),
           ("A. Condensation", "B. Sublimation", "C. Evaporation", "D. Melting")
          )

answers = ("C", "B", "B", "C", "C")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("----------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1

print("----------------------------------------------------------------------")
print("                             RESULTS                                  ")
print("----------------------------------------------------------------------")

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")