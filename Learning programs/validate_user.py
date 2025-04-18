#validate user input exercise

#1. Username is no more than 12 characters
#2. Username must not contain spaces
#3. Username must not contain digits

username = input("Enter your username: ")

if len(username) >= 12:
    print(f"{username} is too long. The username cannot be longer than 12 characters long!")
elif username.find(" ") != -1:
    print(f"{username} contains whitespaces. The username cannot contain whitespaces!")
elif not username.isalpha():
    print(f"{username} contains digits. The username cannot contain digits!")
else:
    print(f"The username you have chosen is okay 😎. Welcome {username}")