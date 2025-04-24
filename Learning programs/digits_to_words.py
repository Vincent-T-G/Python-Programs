#Problem statement: Write a program that takes input in digits and displays the numbers in words

numbers =   { 
                "1" : "one",
                "2" : "two",
                "3" : "three",
                "4": "four",
                "5" : "five",
                "6" : "six",
                "7" : "seven",
                "8" : "eight",
                "9" : "nine",
                "0" : "zero"
            }

phone = input("Phone: ")

print(f"Your phone number in words is: ")

for i in range(len(phone)):
    print(numbers.get(phone[i]), end = " ")