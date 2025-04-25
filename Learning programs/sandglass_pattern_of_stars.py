#Problem statement: write a program that displays the following sandglass pyramid of stars

# * * * * * 
#  * * * *
#   * * * 
#    * * 
#     *   
#    * *
#   * * *
#  * * * *
# * * * * *

def get_length():
    set = False
    while not set:
        try:
            length = int(input("Enter the length of the hourglass (even): "))

            if length % 2 == 0:
                set = True
            else:
                print("The length must be an even number!")
        except ValueError:
            print("Please enter a numerical digit!!")

    return length
        

length = int(get_length()/2)

for i in reversed(range(1,length+1)):
    space = length-i
    for x in range(1,space+1):
        print(" ",end = "")
    for c in range(i):
        print("* ",end = "")
    print()

for i in range(1,length+1):
    space = length-i
    for x in range(1,space+1):
        print(" ",end = "")
    for c in range(i):
        print("* ",end = "")
    print()
