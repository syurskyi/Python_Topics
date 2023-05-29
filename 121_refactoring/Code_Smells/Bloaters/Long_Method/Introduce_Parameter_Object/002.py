# Problem

def calculatePayroll(hoursWorked, hourlyRate):
    totalPay = hoursWorked * hourlyRate
    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        overtimePay = overtimeHours * (hourlyRate * 1.5)
        totalPay += overtimePay
    return totalPay

# Solution

class Employee:
    def __init__(self, hoursWorked, hourlyRate):
        self.hoursWorked = hoursWorked
        self.hourlyRate = hourlyRate

    def calculatePayroll(self):
        totalPay = self.basePay()
        if self.hoursWorked > 40:
            overtimeHours = self.hoursWorked - 40
            overtimePay = overtimeHours * (self.hourlyRate * 1.5)
            totalPay += overtimePay
        return totalPay

    def basePay(self):
        return self.hoursWorked * self.hourlyRate

# In these examples, the initial code calculates values based on multiple parameters.
# By introducing a parameter object (i.e., a class) that encapsulates the relevant data,
# the code becomes more organized and readable. The calculations are now part of the parameter object's methods,
# making it easier to manage and maintain the logic associated with the specific domain.