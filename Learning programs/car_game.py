#This is part one of the car game projects where the user inputs commands and the program responds accordingly 
#with the commands being, start, stop and quit as well as help


while True:
    command = input("> ").lower()
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        print()
    elif command == "start":
        print("Car started...Ready to go!")
    elif command == "stop":
        print("Car stopped.")
    elif command == "quit":
        break
    else:
        print("I do not understand that...")