#Problem statement: Write a program to find the largest number in a list

numbers = [3,4,6,23,101,5,25,68,53]

largest = 0

for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number in the list is {largest}")