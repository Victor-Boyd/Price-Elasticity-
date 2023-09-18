import math

# Input values
price1 = 175
price2 = 225
quantity1 = 36
quantity2 = 28

# Calculating the midpoint of price and quantity
midpointprice = (price1 + price2) / 2
midpointquantity = (quantity1 + quantity2) / 2

# Calculating percentage change in quantity demanded
quantitypercentagechange = (quantity2 - quantity1) / midpointquantity

print ("Percent change in quantity =",quantitypercentagechange*100,"%")

# Calculating percentage change in price
pricepercentagechange = (price2 - price1) / midpointprice

print ("Percent change in price =",pricepercentagechange*100,"%")

# Calculating Price elasticity
priceelasticity = quantitypercentagechange / pricepercentagechange

# Print Price elasticity
print(priceelasticity)

if abs(priceelasticity) > 1:
    print ("Price is elastic")
elif abs(priceelasticity) == 1:
    print ("Price is unit elastic")
else:
    print ("Price is not elastic")
