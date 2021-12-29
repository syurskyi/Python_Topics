import math
def round_even(number):
    """Takes a number and returns it rounded even"""
    

    if (number * 10) % 10 == 5:
        below = int(number)
        return below if below % 2 == 0 else math.ceil(number)

    return round(number)








