#This is python project number 16
#TITLE:SLOT MACHINE

#It's a slot machine program using python

import random

def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","⭐"]
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[0] == "🍉":
            return bet*4
        elif row[0] == "🍋":
            return bet*5
        elif row[0] == "🔔":
            return bet*10
        else:
            return bet*20
    
    return 0

def main():
    balance = 100

    print("*******************************************")
    print("    Welcome to Vincent's Slot Machine")
    print("       Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*******************************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        print()
        bet = input("What amount would you like to bet: ")

        if not bet.isdigit():
            print()
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("      Please enter a valid number")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print()
            continue

        bet = int(bet)

        if bet > balance:
            print()
            print("Insufficient balance!!")
            print()
            continue

        if bet <= 0:
            print()
            print("Bet must be greater than 0")
            print()
            continue

        balance -= bet

        row = spin_row()
        print()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won: ${payout}")
        else:
            print("Sorry! You lost this round")

        balance += payout

        play_again = input("Do you want to play again? (Y|N): ").upper()

        if play_again != "Y":
            break

    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")
    
if __name__ == "__main__":
    main()


