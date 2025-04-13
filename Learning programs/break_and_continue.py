#This program was written in the learning of break and continue statements in python

#BREAK STATEMENT

#The code below generates a list with the numbers from 0 to 99 
#and then uses a for loop to print the numbers all the way up to 50

numbers = list(range(0,100))

for number in numbers:
    if number > 50:
        break
    print(number, end = " ")

print("")

#The break is also used to break an infinite while loop if a certain condition is activated like before

while True:
    num = input("Enter the number (q to quit): ")
    if num == 'q':
        break
    print(num)

#CONTINUE STATEMENT

#The code below is used to print the numbers 0,1 and 3 
#The code uses a for loop with the range function which gives us 0 to 4 
#then uses continue statement to skip when the number is 2 or 4

for i in range(5):
    if i == 2 or i == 4:
        continue
    print(i)

print("Even numbers")


n = 0

while n<=10:
    n+=1
    if n % 2 != 0:
        continue
    print(n, end = " ")