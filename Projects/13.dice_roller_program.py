#This is python project number 13
#TITLE:DICE GAME

#It's a dice roller game program using python

import random


#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")... 
#print this and they give you the symbols you see below in the terminal
# ● ┌ ─ ┐ │ └ ┘


dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

num_of_dice = int(input("How many dice do you want to roll?: "))
total = 0
'''

#PRINT VERTICALLY

for x in range(num_of_dice):
    choice = random.randint(1,6)
    for i in range(5):
        print(dice_art.get(choice)[i])
    total += choice
print()
print(f"You got a total of: {total}") 

'''


#PRINT HORIZONTALLY

dice = []

for i in range(num_of_dice):
    choice = random.randint(1,6)
    dice.append(choice)
    total += choice

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

print()
print(f"You got a total of: {total}")
