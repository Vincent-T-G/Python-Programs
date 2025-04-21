#This is python project number 8
#TITLE:CAR GAME

#It's a car game program using python

state = "off"

while True:
    command = input("> ").lower()
    
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        print()
    elif command == "start" and state == "off":
        state = "on"
        print("Car started...Ready to go!")
    elif command == "stop" and state == "on":
        state = "off"
        print("Car stopped.")
    elif command == "start" and state == "on":
        print("Car is already on")
    elif command == "stop" and state == "off":
        print("Car is already off")
    elif command == "quit":
        break
    else:
        print("I do not understand that...")