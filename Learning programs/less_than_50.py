#This program is written in he process of learning how to use if statements in python

#variables to be used in the if statements
x = 10
y = 60

#The statement below shows an if statement with a print statement that executes if the condition returns true

if x < 50:
    print("x is less than 50")

#Below show that the statement outside of the if block executes irregardless of the if statement returning true or false

if y < 50:
    print("y is less than 50")
print("End of section")

#The statement below shows the shorthand if
#If there's only one statement in the if block you can just put it in the same line

if x < 50: print("x is less than 50")
print("End of section")

#The statements below show the nested if statements structure

if x < 50:
    if x == 10:
        print("x is equal to 10")
    print("x is less than 50")
print("End of section")