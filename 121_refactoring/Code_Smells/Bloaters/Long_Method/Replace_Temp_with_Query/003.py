# Problem

def calculateSalary():
    baseSalary = hoursWorked * hourlyRate
    overtime = 0
    if hoursWorked > 40:
        overtime = (hoursWorked - 40) * hourlyRate * 1.5

    totalSalary = baseSalary + overtime
    return totalSalary


# Solution

def calculateSalary():
    totalSalary = baseSalary() + overtime()
    return totalSalary

def baseSalary():
    return hoursWorked * hourlyRate

def overtime():
    if hoursWorked > 40:
        return (hoursWorked - 40) * hourlyRate * 1.5
    else:
        return 0

# In the problem example, the variables baseSalary and overtime are used as temporary variables to store
# the respective calculations. In the solution example, we eliminate these temporary variables by extracting
# the calculations into separate functions baseSalary() and overtime(), which return the calculated values based
# on the hours worked and hourly rate.