#This code is written in understanding how to reverse the range of numbers when using the range function in a for loop
#The code below uses a for loop with the range function to print the numbers from 5 to 1

for i in range(5,0,-1):
    print(i)
print("Section done!")

#We can also do this using the reversed() function

for i in reversed(range(1,6,1)):
    print(i)
print("Done!")