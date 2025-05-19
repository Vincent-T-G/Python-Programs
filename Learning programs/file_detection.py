# This program is written in the learning and practice of file detection in python

import os

file_path = "Projects"

# file_path = "transactions.xlsx"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("The location doesn't exist")