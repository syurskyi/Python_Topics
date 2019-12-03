# Trapping Constraints but Not Errors
def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2

f(1) # error

def reciprocal(x):
    assert x != 0              # A useless assert!
    return 1 / x               # Python checks for zero automatically