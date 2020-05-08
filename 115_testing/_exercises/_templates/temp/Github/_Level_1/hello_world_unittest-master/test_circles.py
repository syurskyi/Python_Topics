import unittest
from circles import circle_area
from math import pi

c_ TestCircleArea(unittest.TestCase):
    ___ test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    ___ test_values(self):
        self.assertRaises(ValueError, circle_area, -2)

    ___ test_types(self):
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")