#Problem statement: Write a program to find the largest number in a list 
#Using modules knowledge to store the function elsewhere and calling it here
#The function to find the largest number is defined in the utils.py module 

import utils

numbers = [3,4,6,23,101,5,25,68,53]

largest = utils.find_max(numbers)

print(f"The largest number in the list is {largest}")