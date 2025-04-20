#Problem statement: Write a program to print the multiplication table pattern as shown:

#1
#2 4
#3 6 9
#4 8 12 16
#5 10 15 20 25


length = int(input("Enter the number of rows: "))


for i in range(1,length+1):
    for x in range(1,i+1):
        print(i*x , end = " ")
    print()