#This program is written in the learning of how to use logical AND to combine conditions
#The program checks that the age of the user is above 18 and below 30 and if the nationality is Kenyan or South African
# and if so prints the the user is eligible for an exam along with the fees to be paid

age = 20
nationality = "South African"

if age > 18 and age < 30 and nationality == "Kenyan":
    print("The user is eligible for the exam. The exam fee is kes 2,000")
if age > 18 and age < 30 and nationality == "South African":
    print("The user is eligible for the exam. The exam fee is 600 rand")
else:
    print("You are not eligible for the exam")