# Problem

def calculateTotal():
    subtotal = quantity * unitPrice
    tax = 0
    if subtotal > 1000:
        tax = subtotal * 0.1

    total = subtotal + tax
    return total

# Solution

def calculateTotal():
    total = subtotal() + tax()
    return total

def subtotal():
    return quantity * unitPrice

def tax():
    if subtotal() > 1000:
        return subtotal() * 0.1
    else:
        return 0

# In this example, we have temporary variables subtotal and tax storing the respective calculations.
# By extracting these calculations into separate functions subtotal() and tax(), we eliminate
# the need for temporary variables and simplify the code.
#
# By using the "Replace Temp with Query" refactoring technique, we eliminate the need for temporary variables
# and make the code more readable and maintainable.