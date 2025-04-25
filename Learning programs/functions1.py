#This program was written in the learning of functions in python

def greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


def square(number):
    return number*number


print("Start")
greet_user("John","Smith")
# greet_user(last_name="Jane",first_name="Mary")
number = int(input("Enter the number you want to square: "))
#result = square(number)
print(f"The square of {number} is {square(number)}")
print("Finish")