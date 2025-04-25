#Problem statement: write a program that displays the following right pyramid of stars
# *  
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * * 
# * * 
# * 

length = int(input("Enter the length(odd): "))

while length % 2 == 0:
    print("The length must be an odd number!")
    print()
    length = int(input("Enter the length(odd): "))

peak = length // 2 + 1

for i in range(1,peak+1):
    for x in range(i):
        print("* ", end = "")
    print()
for i in reversed(range(1,peak)):
    for x in range(i):
        print("* ", end = "")
    print()