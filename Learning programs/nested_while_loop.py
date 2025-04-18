#This program is written in the learning of the use of nested while loops

#The code below iterates through two lists and prints all the different combinations of the two lists

list1 = [1,2,3]
list2 = [4,5,6]

i = 0

while i < len(list1):
    j = 0
    while j < len(list2):
        print(list1[i],list2[j])
        j += 1
    print()
    i += 1