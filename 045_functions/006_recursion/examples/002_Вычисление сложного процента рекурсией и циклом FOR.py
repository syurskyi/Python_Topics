durationInYears = 10
interestRate = .06
compoundedPerYear = 12
principalAmount = 4000

# for


# def compoundInterest(principal, compounded, duration, rate):
#     totalCompounded = duration * compounded
#     for i in range(1, (totalCompounded+1)):
#         principal = principal*(1+(rate/compounded))
#     return principal
#
#
# print(compoundInterest(principalAmount, compoundedPerYear, durationInYears, interestRate))

# recursion

#
def compoundRecursion(principal, compounded, duration, rate, numberOfRecursions):
    if numberOfRecursions == 0:
        totalDuration = compounded * duration
    elif numberOfRecursions != 0:
        totalDuration = duration
    if duration == 0:
        return principal
    else:
        newDuration = totalDuration - 1
        amount = principal*(1+(rate/compounded))
        return compoundRecursion(amount, compounded, newDuration, rate, 1)

print (compoundRecursion(principalAmount, compoundedPerYear, durationInYears, interestRate, 0))