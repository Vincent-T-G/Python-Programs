#Problem statement: A house is worth 1M. 
#If the buyer has good credit then they need 10% downpayment but if they have bad credit then they need a 20% downpayment
#Print the downpayment for a buyer with good credit

house_value = 1000000

has_good_credit = True
downpayment_g = house_value * 0.1
downpayment_b = house_value * 0.2

if has_good_credit:
    print("The buyer has good credit")
    print(f"The required downpayment is ksh.{downpayment_g :,}")
else:
    print("The buyer doesn't have good credit")
    print(f"The required downpayment is ksh.{downpayment_b :,}")