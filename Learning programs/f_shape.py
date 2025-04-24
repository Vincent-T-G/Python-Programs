#Problem statement using the list below, write a nested for loop that prints an F of x's on the screen
#with the numbers in the list representing the number of x's in each row

numbers = [5,2,5,2,2]

for number in numbers:
    for i in range(number):
        print("x", end = "")
    print()