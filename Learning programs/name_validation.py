#The code below checks a name to restrict based on certain conditions
#If the name is less that 3 xters long... says name has to be atleast 3 xters long
#If the name is more that 50 xters long... says name has to be less than 50 xters long
#Otherwise it says it looks good

name = 'Jonathan'

if len(name) < 3:
    print("The name has to be more than three characters long!")
elif len(name) > 50:
    print("The name cannot be more than fifty characters long")
else:
    print(f"Your name is {name}")
    print("The name looks good")