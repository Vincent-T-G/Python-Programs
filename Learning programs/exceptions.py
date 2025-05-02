#This code is written in the understanding of exceptions and error handling using try except construct

try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("The age cannot be zero")