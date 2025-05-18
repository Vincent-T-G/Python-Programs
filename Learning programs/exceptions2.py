# This program is a program written in the learning and practice of handling exceptions in python

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide a number by zero!")
except ValueError:
    print("Please only enter a number!")
except Exception:
    print("Something went wrong!")
finally:
    print("Clean up afterwards")