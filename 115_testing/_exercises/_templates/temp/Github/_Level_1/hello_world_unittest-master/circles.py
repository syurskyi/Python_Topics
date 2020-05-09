____ math ______ pi

___ circle_area(r
    __ type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")

    __ r < 0:
        raise ValueError("The radius cannot be negative")
    r_ pi*(r**2)