import unittest
from math import pi, sin, cos
from shapes import ShapesArea

class TestShapes(unittest.TestCase):
    def test_value_check(self):
        # Check value of number that the user entered and make sure it is in the valid range (>0)
        self.assertRaises(ValueError, ShapesArea().value_check, -1)
        self.assertRaises(ValueError, ShapesArea().value_check, -100.3454)

    def test_type_check(self):
        # Check type of the information entered and raise/catch error
        self.assertRaises(TypeError, ShapesArea().value_check, True)
        self.assertRaises(TypeError, ShapesArea().value_check, "Text")
        self.assertRaises(TypeError, ShapesArea().value_check, 3+6j)

    def test_circle_area_value(self):
        # Check and confirm function is calculating the circle area value properly
        self.assertAlmostEqual(ShapesArea().circle_area(2), pi*2**2)
        self.assertAlmostEqual(ShapesArea().circle_area(0), 0)
        self.assertAlmostEqual(ShapesArea().circle_area(100.55343), pi*100.55343**2)

    def test_triangle_area_value(self):
        # Check and confirm function is calculating the triangle area value properly
        self.assertAlmostEqual(ShapesArea().triangle_area(2), 1/2*(2*sin(pi/3)+2)*(2*cos(pi/3)))
        self.assertAlmostEqual(ShapesArea().triangle_area(0), 0)
        self.assertAlmostEqual(ShapesArea().triangle_area(12.2323), 1/2*(12.2323*sin(pi/3)+12.2323)*(12.2323*cos(pi/3)))        

    def test_square_area_value(self):
        # Check and confirm function is calculating the square area value properly
        self.assertAlmostEqual(ShapesArea().square_area(2), 2*2*sin(pi/4))
        self.assertAlmostEqual(ShapesArea().square_area(0), 0)
        self.assertAlmostEqual(ShapesArea().square_area(100.23434), 2*100.23434*sin(pi/4))
    
        
