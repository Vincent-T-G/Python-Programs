#Problem statement: Write a program that calculates the sum of the first n natural numbers using a for loop
#Natural numbers are all positive numbers starting from 1 onwards
#The value of N is gotten from the user and the value stored in a variable

n = int(input("Enter the value of n: "))

#variable to store the sum

sum = 0

#for loop to add the natural numbers 

for i in range(1,n+1):
    sum +=i
print(f"The sum of the first {n} natural numbers is {sum}")