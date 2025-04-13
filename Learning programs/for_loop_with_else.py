#This code was written in the process of learning how to write for loops with else

#The code below iterates through the list of languages looking for Java

fav_languages = ['Python', 'C', 'Java', 'Ruby']

for language in fav_languages:
    if language == 'Java':
        print("I like Java.")
        break
else:
    print("I don't like Java.")