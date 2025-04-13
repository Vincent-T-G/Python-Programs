#This program is written in the learning of how to use for loops with lists
#The code below iterates over a list of cars and prints the names of the cars in the list

cars = ['Audi', 'BMW', 'Toyota']
print('Printing with in:')
for car in cars:
    print(car)

#This can also be done using a for loop with the range function


print('And with range function:')
times = len(cars)

for i in range(0,times,1):
    print(cars[i])

#list comprehension

print('And with list comprehension:')
[print(car) for car in cars]