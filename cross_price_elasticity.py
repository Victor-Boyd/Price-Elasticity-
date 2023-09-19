import math

# for XED use the change of quantity demanded of product x and the change of price demanded of product y


# Input values
price1 = 200
price2 = 160
quantity1 = 300
quantity2 = 340


# Calculating the midpoint of price and quantity
midpoint_quantity = (quantity1 + quantity2) / 2
midpoint_price = (price1 + price2) / 2

# Calculating percentage change in quantity demanded
quantity_percentage_change_producty = ((quantity2 - quantity1) / midpoint_quantity) * 100

print("Percent change in quantity =", quantity_percentage_change_producty, "%")

# Calculating percentage change in price
price_percentage_change_productx = ((price2 - price1) / midpoint_price) * 100

print("Percent change in price =", price_percentage_change_productx, "%")

# Calculating price elasticity
price_elasticity = quantity_percentage_change_producty / price_percentage_change_productx

# Calculating Price elasticity
cross_price_elasticity = quantity_percentage_change_producty / price_percentage_change_productx

# Print Price elasticity
print(cross_price_elasticity)

if cross_price_elasticity > 0:
    print("Goods are substitutes")
elif cross_price_elasticity < 0:
    print("Goods are complements")
else:
    print("Goods are unrelated")