#Problem statement: write a program that displays the following pascal's triangle

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

import math

def get_length():
    set = False
    while not set:
        try:
            length = int(input("Enter the length of the pascal's triangle: "))
            set = True
        except ValueError:
            print("Please enter a numerical digit!!")

    return length
        
length = get_length()


for i in range(length):
    space = length - (i+1)
    for v in range(space):
        print(" ",end = "")
    for x in range(i+1):
        ans = int(math.factorial(i)/(math.factorial(x)*math.factorial(i-x)))
        print(ans, end=" ")
    print()
    