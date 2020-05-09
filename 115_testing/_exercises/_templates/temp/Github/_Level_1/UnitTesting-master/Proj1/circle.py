____ math ______ pi

___ circle_area(r
    if type(r) not in [int, float]:
        raise TypeError("Make sure the radius is a positive real number.")
    if r < 0:
        raise ValueError("The radius must be a number greater than 0.")
    r_ pi*(r**2)


___ circle_circumfrence(r
    if type(r) not in [int, float]:
        raise TypeError("Make sure the radius is a positive real number.")
    if r < 0:
        raise ValueError("The radius must be a number greater than 0.")
    r_ pi*r*2