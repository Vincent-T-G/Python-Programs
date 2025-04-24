#This is python project number 12
#TITLE:ROCK PAPER SCISSORS

#It's a rock paper scissors game program using python

import random

print("---------------------------- Welcome to the rock, paper, scissors game ----------------------------")

options = ("rock", "paper", "scissors")

player = None



running = True

score = 0
draw = 0
loss = 0
total = 0

while running:
    computer = random.choice(options)
    player = None
    while player not in options and player != "q":
        player = input("Enter a choice (rock,paper,scissors)(q to quit): ").lower()
    if player == "q":
        running = False
    else:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player == computer:
            print("It's a tie!")
            draw += 1
            total += 1
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            print("You win!")
            score += 1
            total += 1
        else:
            print("You lose!")
            total += 1
            loss += 1

print()
print("------------------------------------- RESULTS -------------------------------------")
print(f"You played {total} games")
print(f"Your score is: {score} win(s), {draw} draw(s) and {loss} loss(s)")
print("Thanks for playing!")