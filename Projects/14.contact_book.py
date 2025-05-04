#This is python project number 14
#TITLE:CONTACT BOOK

#It's a contact book program using python

'''
The contact book has the following functionality
1.Add new contact
2.Search contacts
3.Display contacts
4.Edit contacts
5.Delete contacts
6.Exit
'''

contacts = {"John Kamau" : "0712345678", "Peter Mwangi" : "0787654321"}


choice = 0

print("--------------------------------------------------------")

print("-----------   Welcome to your contacts app   -----------")

print("--------------------------------------------------------")

while True:
    print("Pick which operation you would like to perform: ")
    print()
    print("1.Add new contact")
    print("2.Search contacts")
    print("3.Display contacts")
    print("4.Edit contacts")
    print("5.Delete contacts")
    print("6.Exit")
    print()
    choice = input("-->")

    match choice:
        case "1":
            name = input("Enter the name of the contact: ")
            number = input("Enter the phone number of the contact above: ")
            contacts[name] = number
            print()
            print("------------------------------------------------------------------")
            print(f"New contact: {name} : {number} has been added succesfully")
            print("------------------------------------------------------------------")
            print()
        case "2":
            found = 0
            search = input("Enter the name of the contact you want to find: ")
            print()
            print("--------------------------------------------------------")
            for key, value in contacts.items():
                if key == search:
                    print(f"{key} : {value}")
                    found += 1
            if found == 0: print(f"{search} is not a contact in your contact list")
            print("--------------------------------------------------------")
            print()
        case "3":
            print()
            print("--------------------------------------------------------")
            print("-------------------   CONTACT LIST   -------------------")
            print("--------------------------------------------------------")
            print()
            i=1
            for key, value in contacts.items():
                print(f"{i}.{key} : {value}")
                i+=1

            print()
            print("--------------------------------------------------------")
            print()
        case "4":
            found = 0
            print()
            search = input("Enter the name of the contact you want to edit: ")
            new_no = input("Enter their new phone number: ")
            print()
            print("--------------------------------------------------------")
            for key, value in contacts.items():
                if key == search:
                    contacts[key] = new_no
                    print(f"{key} now has the number: {new_no}")
                    found += 1
            if found == 0: print(f"{search} is not a contact in your contact list")
            print("--------------------------------------------------------")
            print()
        case "5":
            found = 0
            print()
            search = input("Enter the name of the contact you want to delete: ")
            print()
            print("--------------------------------------------------------")
            for key in contacts.keys():
                if key == search:
                    print(f"{key} has now been deleted")
                    found += 1
            if found == 1:
                del(contacts[search])
            else:
                print(f"{search} is not a contact in your contact list")
            print("--------------------------------------------------------")
            print()
        case "6":
            print()
            print("--------------------------------------------------------")
            print("Thank you for using the contacts app 😁")
            print("--------------------------------------------------------")
            print()
            break
        case _:
            print("Invalid choice!!")
            print()
            print("Please pick a number between 1 to 6 depending on your choice")
            print()