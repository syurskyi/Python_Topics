from math import pi, cos, sin

c_ ShapesArea:
    ___  - (self):
        pass

    ___ value_check  r):
        # Check to make sure user input is of acceptable type and value
        if type(r) not in [float, int]:
            raise TypeError("Please enter a valid number greater than 0.")
        if r < 0:
            raise ValueError("Length from center to edge must be greater than 0.")
        
    ___ circle_area  r):
        # Calculate the area of a circle with radius r
        self.value_check(r)
        return pi*(r**2)
    
    ___ triangle_area  r):
        # Calculate the area of an equilateral triangle with center to corner length r
        self.value_check(r)
        return 1/2*(r*sin(pi/3)+r)*(r*cos(pi/3))

    ___ square_area  r):
        # Calculate the area of a square with center to corner length r
        self.value_check(r)
        return 2*r*sin(pi/4)
