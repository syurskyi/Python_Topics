# Problem

def calculateCommission(salesAmount):
    commissionRate = 0.1
    if salesAmount > 10000:
        commissionRate = 0.15
    commission = salesAmount * commissionRate
    return commission

# Solution

class SalesPerson:
    def __init__(self, salesAmount):
        self.salesAmount = salesAmount

    def calculateCommission(self):
        commissionRate = self.commissionRate()
        commission = self.salesAmount * commissionRate
        return commission

    def commissionRate(self):
        if self.salesAmount > 10000:
            return 0.15
        return 0.1

# In these examples, the initial code calculates values based on multiple parameters.
# By introducing a parameter object (i.e., a class) that encapsulates the relevant data,
# the code becomes more organized and readable. The calculations are now part of the parameter object's methods,
# making it easier to manage and maintain the logic associated with the specific domain.