# This program is written in the learning and practicing of writing to files in a pythin script

import json
import csv

data = "I like pizza"

data2 = {"name" : "Spongebob", "age" : 30, "job" : "cook"}

data3 = [
            ["Name", "Age", "Job"],
            ["Spongebob", 30, "Cook"],
            ["Patric", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]
        ]

file_path = "learning programs/output.txt"
file_path2 = "learning programs/output.json"
file_path3 = "learning programs/output.csv"


with open(file_path, "a") as file:
    file.write("\n" + data)
    print(f"text file '{file_path}' was created successfully!")

with open(file_path2, "w") as file2:
    json.dump(data2, file2, indent = 4)
    print(f"json file '{file_path2}' was created successfully!")

with open(file_path3, "w", newline = "") as file3:
    writer = csv.writer(file3)
    for row in data3:
        writer.writerow(row)
    print(f"csv file '{file_path3}' was created successfully!")
