#This code was written in the process of understanding for loops for strings
#The code below prints all the character in a string using a for loop

name = "John"
for c in name:
    print(c, end=" ")
#This prints the the string in the same line and puts a whitespace after each character

print("")

#To access the string in reverse order we can use slicing with a negative step value

for c in name[::-1]:
    print(c, end=" ")

#To split a string into words we use the split() function
#The code below splits a string into words and counts the number of words that were there in the string

print("")

sentence = "Lorem ipsum dolor sit amet, consectetur."
count = 0
for word in sentence.split():
    count +=1
print(f"There are {count} words in the sentence")