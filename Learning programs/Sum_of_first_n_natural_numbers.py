#Problem statement: Write a program that calculates the sum of the first n natural numbers
#Natural numbers are all positive numbers starting from 1 onwards
#The value of N is gotten from the user and the value stored in a variable


#we get the value of in from the user and use the int method to turn it from a string into an integer
n = int(input("Enter the value of n: "))


#store a copy of n to be used in printing at the end
v = n


#we initialise a value to use in the loop to store the sum of the natural numbers
sum = 0


#The while loop that adds the natural numbers 
while n>0:
    sum += n
    n-=1


#Then we print the result
print(f"The sum of the first {v} natural numbers is {sum}")