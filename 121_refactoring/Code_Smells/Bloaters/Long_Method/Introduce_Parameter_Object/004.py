# Problem

def calculateShippingCost(weight, shippingMethod):
    rate = 0.0
    if shippingMethod == 'Standard':
        rate = 5.0
    elif shippingMethod == 'Express':
        rate = 10.0
    cost = weight * rate
    return cost


# Solution

class Shipping:
    def __init__(self, weight, shippingMethod):
        self.weight = weight
        self.shippingMethod = shippingMethod

    def calculateShippingCost(self):
        rate = self.shippingRate()
        cost = self.weight * rate
        return cost

    def shippingRate(self):
        if self.shippingMethod == 'Standard':
            return 5.0
        elif self.shippingMethod == 'Express':
            return 10.0
        return 0.0

# In these examples, the initial code calculates values based on multiple parameters.
# By introducing a parameter object (i.e., a class) that encapsulates the relevant data,
# the code becomes more organized and readable. The calculations are now part of the parameter object's methods,
# making it easier to manage and maintain the logic associated with the specific domain.

