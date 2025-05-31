# Problem statement: Write a program that accepts a string and counts the number of digits letters and special characters in that # string

digits = 0
letters = 0
sp_chars = 0

string = input("Enter the string to be evaluated: ")

for char in string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
    else:
        sp_chars += 1


print()
print(f"{string} has {digits} digits, {letters} letters and {sp_chars} special characters")