# Problem

def calculateTotalAmount():
    subtotal = calculateSubtotal()
    taxRate = getTaxRate()

    taxAmount = subtotal * taxRate
    totalAmount = subtotal + taxAmount

    return totalAmount

def calculateSubtotal():
    pass
    # calculation logic for subtotal

def getTaxRate():
    pass
    # logic to fetch tax rate from database or configuration



# Solution

def calculateTotalAmount():
    subtotal = calculateSubtotal()
    taxAmount = calculateTaxAmount(subtotal)
    totalAmount = subtotal + taxAmount

    return totalAmount

def calculateSubtotal():
    pass
    # calculation logic for subtotal

def calculateTaxAmount(subtotal):
    taxRate = getTaxRate()
    return subtotal * taxRate

 def getTaxRate():
     pass
     # logic to fetch tax rate from database or configuration


# In this example, we extract the calculation of the tax amount into a separate function calculateTaxAmount().
# This function takes the subtotal as a parameter and calculates the tax amount based on the tax rate fetched
# from the getTaxRate() function. This improves code modularity and readability.