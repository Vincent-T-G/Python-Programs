#This program is written in understanding how to use break keyword to end an infinite while loop

while True:
    line = input("Enter a number/string (type 'q' to quit): ")
    if line == 'q':
        break
    print(line)