import math



# Input values
price1 = 15
price2 = 25
quantity_supllied1 = 5
quantity_supplied2 = 14

# Calculating the midpoint of price and quantity
midpoint_price = (price1 + price2) / 2
midpoint_quantity = (quantity_supllied1 + quantity_supplied2) / 2

# Calculating percentage change in quantity demanded
quantity_supplied_percentage_change = (quantity_supplied2 - quantity_supllied1) / midpoint_quantity

print ("Percent change in quantity demanded =",quantity_supplied_percentage_change*100,"%")

# Calculating percentage change in price
price_percentage_change = (price2 - price1) / midpoint_price

print ("Percent change in price =",price_percentage_change*100,"%")

# Calculating Price elasticity
price_elasticity = quantity_supplied_percentage_change / price_percentage_change

# Print Price elasticity
print(price_elasticity)

if abs(price_elasticity) > 1:
    print ("Price is elastic")
elif abs(price_elasticity) == 1:
    print ("Price is unit elastic")
else:
    print ("Price is not elastic")