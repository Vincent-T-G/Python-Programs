#This is python project number 4
#TITLE:TEMPERATURE CONVERTER PROGRAM

#It's a temperature conversion program using python

unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"This temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"This temperature in Celcius is: {temp}°C")
else:
    print(f"{unit} is not a valid unit of measurement")