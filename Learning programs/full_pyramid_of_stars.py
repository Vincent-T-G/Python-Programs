#Problem statement: write a program that displays the following full pyramid of stars
#     *  
#    * *
#   * * *
#  * * * *
# * * * * *

length = int(input("Enter the length of the pyramid: "))


for i in range(1,length+1):
    for v in range(length-i):
        print(" ",end = "")
    for x in range(i):
        print("* ", end = "")
    print()