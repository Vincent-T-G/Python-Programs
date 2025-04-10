#This program is written while learning the if-else construct
#The code below uses if-else to check the age given and prints out whether the person can vote or not

#variable age used for the condition

age = 20

#if-else construct checking if the age is 18 and above

if age < 18:
    print("You can't vote!")
else:
    print("You can vote !")
print("End of section")

#the section below show the short hand if-else structure

print("You can't vote!") if age < 18 else print("You can vote!")
print("End of section")