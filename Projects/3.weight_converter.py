#This is python project number 3
#TITLE:WEIGHT CONVERTER PROGRAM

#It's a weight conversion program using python

#Take the weight and unit as input from the user

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

#Use if-else to check the unit given and therefore convert into the other one then print the changed weight

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight,2)}{unit}")
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight,2)}{unit}")
else:
    print(f"{unit} was not a valid input")
