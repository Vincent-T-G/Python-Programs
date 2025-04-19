#The program below was written in practice of nested loops 
#to print a certain symbol a certain number of times dependent on user input 
#forming a square or rectangle of the symbol given

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()