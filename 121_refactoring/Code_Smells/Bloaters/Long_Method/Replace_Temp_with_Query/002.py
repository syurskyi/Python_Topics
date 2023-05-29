# Problem
def calculatePrice():
    discount = 0
    if quantity > 100:
        discount = 10
    else:
        discount = 5

    total = quantity * unitPrice
    discountedPrice = total - (total * discount / 100)
    return discountedPric


# Solution

def calculatePrice():
    discountedPrice = quantity * unitPrice - (quantity * unitPrice * getDiscount() / 100)
    return discountedPrice

def getDiscount():
    if quantity > 100:
        return 10
    else:
        return 5

# In the problem example, the variable discount is used as a temporary variable to store the discount value.
# In the solution example, we eliminate the temporary variable by extracting the discount calculation
# into a separate function getDiscount(), which returns the appropriate discount based on the quantity.
# This allows us to simplify the calculation of discountedPrice by directly using the getDiscount() function.
#
# By using the "Replace Temp with Query" refactoring technique, we eliminate the need for temporary variables
# and make the code more readable and maintainable.
