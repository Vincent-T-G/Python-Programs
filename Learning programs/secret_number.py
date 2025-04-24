#This program has a secret number which in our case is 9 and the user is given three chances to guess what the number is 
#and if the user gets it they win, however if they take three guesses and don't get it they fail

secret_number = 9

guess_count = 0
guess_limit = 3
while guess_count<guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you have failed!")