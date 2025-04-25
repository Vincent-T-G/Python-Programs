#Problem statement: Write a program to remove the duplicate values in a list

numbers = [1,3,6,3,8,9,5,7,5]
numbers2 = []

for number in numbers:
    if number not in numbers2:
        numbers2.append(number)

print(numbers2)