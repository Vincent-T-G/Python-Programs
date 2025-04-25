#This program uses the knowledge of 2D collections to create a number pad and diplay it on the terminal

characters = ((1,2,3),
              (4,5,6),
              (7,8,9),
              ("*",0,"#"))

for character in characters:
    for sym in character:
        print(sym, end = "   ")
    print()