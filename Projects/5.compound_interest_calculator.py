#This is python project number 5
#TITLE:COMPOUND INTEREST CALCULATOR PROGRAM

#It's a compound interest calculator program using python

principle = 0
rate = 0
time =0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break


while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break


while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = principle * (1 + rate / 100) ** time

print()

print(f"After {time} years the total balance you have is Kshs.{total:.2f}")