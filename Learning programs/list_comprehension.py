# This program was written in the process of learning list comprehensions which is an easier way of creating loops

#program below stores the doubles of numbers 1 to 10 in a list using the traditional for loop method
doubles = []

for i in range(1,11):
    doubles.append(i*2)

print(doubles)

#this can be done as shown below for tripples using list comprehension

triples = [x * 3 for x in range(1,11)]

print(triples)

#for squares

squares = [y ** 2 for y in range(1,11)]

print(squares)

#working with strings
#to make all uppercase and to add the first letter of every fruit in another

fruits = ["apple", "orange", "banana", "coconut"]

fruitchars = [fruit[0] for fruit in fruits]
fruits = [fruit.upper() for fruit in fruits]

print(fruitchars)
print(fruits)

#To add the condition part
#Separate into +ve and -ve

numbers = [1,-2,3,-4,5,-6]

positive_nums = [num for num in numbers if num >= 0]

negative_nums = [num for num in numbers if num <= 0]

print(positive_nums)
print(negative_nums)
