# Trapping Constraints but Not Errors
def f(x):
    a__ x < 0, 'x must be negative'
    return x ** 2

f(1) # error

def reciprocal(x):
    a__ x != 0              # A useless a__!
    return 1 / x               # Python checks for zero automatically