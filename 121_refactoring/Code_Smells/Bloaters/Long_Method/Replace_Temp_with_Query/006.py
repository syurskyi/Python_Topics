# Problem

def calculateTotal():
    subtotal = calculateSubtotal()
    discount = 0
    if subtotal > 100:
        discount = subtotal * 0.1

    total = subtotal - discount
    return total

def calculateSubtotal():
    pass
    # calculation logic for subtotal


# Solution

def calculateTotal():
    subtotal = calculateSubtotal()
    discount = calculateDiscount(subtotal)
    total = subtotal - discount
    return total


def calculateSubtotal():
    pass
    # calculation logic for subtotal

def calculateDiscount(subtotal):
    if subtotal > 100:
        return subtotal * 0.1
    else:
        return 0

# In this example, we extract the calculation of the discount into a separate function calculateDiscount().
# This function takes the subtotal as a parameter and returns the discount amount. By doing so, we eliminate
# the temporary variable discount in the main function and improve code clarity.
#
# By applying the "Replace Temp with Query" refactoring technique, we can simplify complex calculations,
# improve code maintainability, and enhance code readability.