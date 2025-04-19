#Problem statement: Write a program to separate even and odd numbers stored in a list into two different lists.

#we'll create a sample list as well as 2 blank lists for the even and odd values

list1 = list(range(1,25))
listodd = []
listeven = []

#variables for iterating through the list using a while loop
times = len(list1)
i = 0

#While loop that uses the modulus to check if a number is divisible by two then adds the number to the correct list
while i < times:
    if list1[i] % 2 == 0:
        listeven.append(list1[i])
    else:
        listodd.append(list1[i])
    i += 1

#Then we print the results
print("The odd list contains: ")
print(listodd)
print()
print("The even list contains: ")
print(listeven)