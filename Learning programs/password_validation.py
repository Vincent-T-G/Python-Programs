# Problem statement: Write a program to check the validity of the password entered by the user with the following requirements:

# Minimum 7 characters
# Maximum 20 characters
# Minimum of 1 capital letter ad 1 small letter
# Atleast 1 number
# Atleast 1 character from [$#@!]

import re

password = input("Enter the password: ")

if len(password) > 7:
    if len(password) < 20:
        if re.search("[A-Z]",password):
            if re.search("[a-z]",password):
                if re.search("[0-9]",password):
                    if re.search("[$#@!]",password):
                        if re.search(r'\s',password):
                            print("The password must not have spaces!")
                        else:
                            print(f"{password} is a valid password")
                    else:
                        print("The password must contain atleast one of the special characters: $, #, @, !")
                else:
                    print("The password must contain a digit!")
            else:
                print("The password must contain a small letter!")
        else:
            print("The password must contain a capital letter!")
    else:
        print("The password must be shorter than 20 characters long!")
else:
    print("The password must be greater than 7 characters long!")