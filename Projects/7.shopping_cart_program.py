#This is python project number 7
#TITLE:SHOPPING CART PROGRAM

#It's a shopping cart program using python

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)


print()
print("-----YOUR CART-----")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total is: ${total:.2f}")
