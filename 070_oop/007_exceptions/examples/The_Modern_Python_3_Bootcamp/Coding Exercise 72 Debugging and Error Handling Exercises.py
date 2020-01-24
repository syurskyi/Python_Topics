# Division Exercise Solution
#
# Here's my version of the divide function:


def divide(a, b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total