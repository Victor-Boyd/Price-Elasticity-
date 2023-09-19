import math

# for XED use the change of quantity demanded of product x and the change of price demanded of product y

# Input values
price_percentage_change_productx = -0.08
quantity_percentage_change_producty = -.08

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