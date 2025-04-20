#Problem statement: Write a program to print a right triangle number pattern as shown:

#1
#22
#333
#4444
#55555


length = int(input("Enter the number of rows: "))


for i in range(1,length+1):
    times = i+1
    for x in range(1,times):
        print(i , end = " ")
    print()