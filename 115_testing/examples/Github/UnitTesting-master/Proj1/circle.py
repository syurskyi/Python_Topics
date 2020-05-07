from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Make sure the radius is a positive real number.")
    if r < 0:
        raise ValueError("The radius must be a number greater than 0.")
    return pi*(r**2)


def circle_circumfrence(r):
    if type(r) not in [int, float]:
        raise TypeError("Make sure the radius is a positive real number.")
    if r < 0:
        raise ValueError("The radius must be a number greater than 0.")
    return pi*r*2