# Problem statement: Write a program to check whether a given number is prime or not

try:
    number = int(input("Enter the number you want to check: "))
    if number > 1:
        for i in range(number-1,0,-1):
            if number%i == 0:
                if i == 1:
                    print(f"{number} is a  prime number")
                else:
                    print(f"{number} is not prime as it is divisible by {i}")
                    break
    else:
        print(f"{number} is not prime. All prime numbers are greater than 1")
except ValueError:
    print("You must enter an integer!")