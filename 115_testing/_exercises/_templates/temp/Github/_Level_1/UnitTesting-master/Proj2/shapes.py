____ math ______ pi, cos, sin

c_ ShapesArea:
    ___  - 
        p..

    ___ value_check  r
        # Check to make sure user input is of acceptable type and value
        __ ty..(r) no. __ [float, __.]:
            r_ T..("Please enter a valid number greater than 0.")
        __ r < 0:
            r_ V..("Length from center to edge must be greater than 0.")
        
    ___ circle_area  r
        # Calculate the area of a circle with radius r
        value_check(r)
        r_ pi*(r**2)
    
    ___ triangle_area  r
        # Calculate the area of an equilateral triangle with center to corner length r
        value_check(r)
        r_ 1/2*(r*sin(pi/3)+r)*(r*cos(pi/3))

    ___ square_area  r
        # Calculate the area of a square with center to corner length r
        value_check(r)
        r_ 2*r*sin(pi/4)
