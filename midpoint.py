import math

# Input values
price1 = 1
price2 = 2
quantity1 = 90
quantity2 = 70

# Calculating the midpoint of price and quantity
midpointprice = (price1 + price2) / 2
midpointquantity = (quantity1 + quantity2) / 2

# Calculating percentage change in quantity demanded
quantitypercentagechange = (quantity2 - quantity1) / midpointquantity

# Calculating percentage change in price
pricepercentagechange = (price2 - price1) / midpointprice

# Calculating Price elasticity
priceelasticity = quantitypercentagechange / pricepercentagechange

# Print Price elasticity
print(priceelasticity)

if priceelasticity >= 1:
    print ("Price is elastic")
else:
    print ("Price is not elastic")