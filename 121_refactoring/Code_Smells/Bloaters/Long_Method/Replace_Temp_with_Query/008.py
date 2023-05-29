# Problem

def calculateTotalCost():
    subtotal = calculateSubtotal()
    shippingCost = calculateShippingCost(subtotal)

    totalCost = subtotal + shippingCost

    return totalCost

def calculateSubtotal():
    pass
    # calculation logic for subtotal

def calculateShippingCost(subtotal):
    if subtotal > 100:
        shippingCost = 10
    else:
        shippingCost = 5

    return shippingCost



# Solution

def calculateTotalCost():
    subtotal = calculateSubtotal()
    shippingCost = calculateShippingCost(subtotal)

    totalCost = subtotal + shippingCost

    return totalCost

def calculateSubtotal():
    pass
    # calculation logic for subtotal

def calculateShippingCost(subtotal):
    if subtotal > 100:
        return 10
    else:
        return 5


# In this example, the calculateShippingCost() function already follows the "Replace Temp with Query" approach.
# It directly returns the shipping cost based on the subtotal without using a temporary variable.
# This improves code readability and eliminates unnecessary complexity.
#
# These examples demonstrate how the "Replace Temp with Query" refactoring technique can be applied
# to more complex scenarios, allowing for better code organization, improved readability,
# and reduced reliance on temporary variables.