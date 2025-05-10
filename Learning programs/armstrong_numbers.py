# Problem Statement: Write a program to check whether a given 3-digit number is an armstrong number

while True:
    number = input("Enter a 3 digit number: ")

    if number.isnumeric():
        if len(number)!=3:
            print("You need to enter a 3-digit number!")
            continue
        else:
            res = 0
            for char in number:
                operand = int(char)
                res += operand**3

            if int(number) == res:
                print(f"{number} is an amstrong number")
                break
            else:
                print(res)
                print(f"{number} is not an amstrong number")
                break
    else:
        print("Invalid input!")
        print("Please enter numeric values only!")
        continue