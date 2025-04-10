#This program is written in the learning of how to use logical OR to combine conditions
#The program checks whether the day is Saturday or Sunday and if it is it prints that it is a holiday, 
# if it's a Monday or Friday then it prints work 2 extra hours else it prints normal working hours

today = "Tuesday"

if today == "Saturday" or today == "Sunday":
    print("It's a holiday!")
elif today == "Monday" or today == "Friday":
    print("Work two extra hours!")
else:
    print("Normal working hours!")