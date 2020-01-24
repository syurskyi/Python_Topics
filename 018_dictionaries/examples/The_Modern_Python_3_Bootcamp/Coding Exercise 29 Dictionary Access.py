# Bakery Dictionary Exercise Solution
#
# REMEMBER, WE HAVE TO USE FORMAT() RATHER THAN F-STRINGS IN THE UDEMY CODE EDITOR!
#
# The following code is common to all solutions:

# This code picks a random food item:
from random import choice  # DON'T CHANGE!

food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# Solution using IN
#
# In the last video, we saw how to use in to test if a value is contained in a dictionary:

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")

# Solution using get()
#
# We can do the same thing using get() and storing the result to a variable.
# The variable will either contain the corresponding value from the dictionary OR None.
# We can write a simple conditional check:

quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")

