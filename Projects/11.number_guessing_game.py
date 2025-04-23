#This is python project number 11
#TITLE:NUMBER GUESSING GAME

#It's a guessing game program using python

import random

low_range = 1
high_range = 150
guesses = 0
is_running = True
answer = random.randint(low_range,high_range)

print("Python Random Number Guessing Game")

print(f"Pick a number between {low_range} and {high_range}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_range or high_range < guess :
            print("The number you have chosen is out of ranges!!")
            print(f"Please pick a number between {low_range} and {high_range}")
        elif guess < answer:
            print("Too low! try again!") 
        elif guess > answer:
            print("Too high! try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"It took you {guesses} tries")
            is_running = False
    else:
        print("Invalid guess!!")
        print(f"Please pick a number between {low_range} and {high_range}")