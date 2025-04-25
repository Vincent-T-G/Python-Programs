#This file contains a utility function to find the largest number given a list of numbers
#Is called in the find_max.py file

def find_max(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest