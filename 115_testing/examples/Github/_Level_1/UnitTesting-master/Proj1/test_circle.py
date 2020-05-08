import unittest
from circle import circle_area
from circle import circle_circumfrence
from math import pi

# https://www.youtube.com/watch?v=1Lfv5tUGsn8

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Tests to confirm that it calculates the area as expected
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2), pi*(2**2))
        self.assertAlmostEqual(circle_area(3.145),pi*(3.145**2))
    
    def test_area_types(self):
        # Test to make sure the correct type is entered into the function
        self.assertRaises(TypeError, circle_area, "Text")
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, 5+3j)

    def test_area_values(self):
        # Test to make sure the incorrect value hasnt been entered
        self.assertRaises(ValueError, circle_area, -3)

    def test_circumfrence(self):
        # Tests circumfrence to expected val
        self.assertAlmostEqual(circle_circumfrence(0), 0)      
        self.assertAlmostEqual(circle_circumfrence(2), 2*pi*2)
        self.assertAlmostEqual(circle_circumfrence(3.14556445), 3.14556445*pi*2)

    def test_circumfrence_types(self):
        # Test circumfrence input to make sure errors handled
        self.assertRaises(TypeError, circle_circumfrence, "Text")
        self.assertRaises(TypeError, circle_circumfrence, True)
        self.assertRaises(TypeError, circle_circumfrence, 3+4j)

    def test_circumfrence_values(self):
        # Test to insure proper type is entered into value
        self.assertRaises(ValueError, circle_circumfrence, -3)
        self.assertRaises(ValueError, circle_circumfrence, -99.23545)







