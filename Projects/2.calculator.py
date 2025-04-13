#This is python project number 2
#TITLE:CALCULATOR PROGRAM

#It's a beginner claculator program using python

#First we take the operator and the operands from the user

num1 = float(input("Enter the first operand: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second operand: "))

#Then we perform the operation depending on the operator chosen and output the result

if operator == "+":
    result = round(num1 + num2,2)
    print(f"The result is {result}.")
elif operator == "-":
    result = round(num1 - num2,2)
    print(f"The result is {result}.")
elif operator == "*":
    result = round(num1 * num2,2)
    print(f"The result is {result}.")
elif operator == "/":
    result = round(num1 / num2,2)
    print(f"The result is {result}.")
else:
    print(f"{operator} is not a valid operator")