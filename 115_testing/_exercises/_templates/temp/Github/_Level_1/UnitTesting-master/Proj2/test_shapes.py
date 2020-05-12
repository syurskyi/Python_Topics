______ u__
____ math ______ pi, sin, cos
____ shapes ______ ShapesArea

c_ TestShapes?.?
    ___ test_value_check
        # Check value of number that the user entered and make sure it is in the valid range (>0)
        aR..(V.., ShapesArea().value_check, -1)
        aR..(V.., ShapesArea().value_check, -100.3454)

    ___ test_type_check
        # Check type of the information entered and raise/catch error
        aR..(T.., ShapesArea().value_check, T..)
        aR..(T.., ShapesArea().value_check, "Text")
        aR..(T.., ShapesArea().value_check, 3+6j)

    ___ test_circle_area_value
        # Check and confirm function is calculating the circle area value properly
        aAE..(ShapesArea().circle_area(2), pi*2**2)
        aAE..(ShapesArea().circle_area(0), 0)
        aAE..(ShapesArea().circle_area(100.55343), pi*100.55343**2)

    ___ test_triangle_area_value
        # Check and confirm function is calculating the triangle area value properly
        aAE..(ShapesArea().triangle_area(2), 1/2*(2*sin(pi/3)+2)*(2*cos(pi/3)))
        aAE..(ShapesArea().triangle_area(0), 0)
        aAE..(ShapesArea().triangle_area(12.2323), 1/2*(12.2323*sin(pi/3)+12.2323)*(12.2323*cos(pi/3)))

    ___ test_square_area_value
        # Check and confirm function is calculating the square area value properly
        aAE..(ShapesArea().square_area(2), 2*2*sin(pi/4))
        aAE..(ShapesArea().square_area(0), 0)
        aAE..(ShapesArea().square_area(100.23434), 2*100.23434*sin(pi/4))
    
        
