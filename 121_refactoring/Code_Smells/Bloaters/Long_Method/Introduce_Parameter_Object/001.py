# Problem

def calculateTotal():
    basePrice = quantity * itemPrice
    if basePrice > 1000:
        return basePrice * 0.95
    else:
        return basePrice * 0.98

# Solution

class Order:
    def __init__(self, quantity, itemPrice):
        self.quantity = quantity
        self.itemPrice = itemPrice

    def calculateTotal(self):
        if self.basePrice() > 1000:
            return self.basePrice() * 0.95
        else:
            return self.basePrice() * 0.98

    def basePrice(self):
        return self.quantity * self.itemPrice

# n the problem example, the calculateTotal function calculates the base price using the quantity and
# itemPrice variables and applies a discount based on the base price value.
# However, this approach can make the code less readable and harder to maintain.
#
# The solution example introduces a new class called Order that encapsulates the quantity and item price
# as its properties. The calculateTotal method is now part of this class. By doing so, we create a parameter object
# that represents the relevant data for calculating the total. This improves code organization and reduces the reliance
# on individual variables, making it easier to manage and understand the calculations associated with an order.
