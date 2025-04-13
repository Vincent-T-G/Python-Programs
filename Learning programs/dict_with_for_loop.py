#This code was written in the process of learning how to use for loops with dictionaries


#The code below iterated over  a dictionaries and prints all the keys in the dictionary

print("Accessing the keys of the dictionary using a for loop")


course = {'name':'Python', 'instructor':'Jaspreet'}
for x in course:
    print(x)

print("Accessing the keys of the dictionary using a for loop and the keys() method")

for x in course.keys():
    print(x)


#To print the values instead of the keys

print("Accessing the values of the dictionary using a for loop")

for x in course:
    print(course[x])

#This can also be done using the values() method

print("Accessing the values of the dictionary using a for loop and the values() method")

for y in course.values():
    print(y)

#To access both the keys and their corresponding values using the items() method

print("Accessing the keys and values of the dictionary using a for loop and the items() method")

for x,y in course.items():
    print(x,y)