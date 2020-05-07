import unittest
from math import exp
from main import Interest

class TestInterest(unittest.TestCase):
    def test_simple_interest_type_error(self):
        """ Test all arguements of the function to determine that if rouge type is entered that it is caught """
        # Arrange (instantiate class)
        # Act (use instantiation)
        # Assert (assert method)
        self.assertRaises(TypeError, Interest().simple_interest, 'init amt', 1, 1)
        self.assertRaises(TypeError, Interest().simple_interest, True, .5, 1)
        self.assertRaises(TypeError, Interest().simple_interest, 1+3j, .5, 1)

        self.assertRaises(TypeError, Interest().simple_interest, 100, 'rate', 1)
        self.assertRaises(TypeError, Interest().simple_interest, 100, True, 1)
        self.assertRaises(TypeError, Interest().simple_interest, 100, 1+3j, 1)

        self.assertRaises(TypeError, Interest().simple_interest, 100, .5, 'time')
        self.assertRaises(TypeError, Interest().simple_interest, 100, .5, True)
        self.assertRaises(TypeError, Interest().simple_interest, 100, .5, 1+3j)

    def test_simple_interest_value_error(self):
        """ Test all arguments of the function to ensure that negatives, non decimals, and negative time durations dont work """
        self.assertRaises(ValueError, Interest().simple_interest, -100, .5, 1)
        self.assertRaises(ValueError, Interest().simple_interest, 100, -.5, 1)
        self.assertRaises(ValueError, Interest().simple_interest, 100, .5, -1)
        self.assertRaises(ValueError, Interest().simple_interest, 100, 1.5, -1)
    
    def test_function_output_correctness(self):
        """ Test and make sure the functions are outputting the expected values """
        self.assertAlmostEqual(Interest().simple_interest(100, .5, 1), 100 * (.5 * 1 + 1))
        self.assertAlmostEqual(Interest().simple_interest(0, .5, 1), 0 * (.5 * 1 + 1))
        self.assertAlmostEqual(Interest().simple_interest(17659, .03, 10), 17659 * (.03 * 10 + 1))

    def test_compound_interest_type_error(self):
        """ Test all arguements of the function to determine that if rouge type is entered that it is caught """
        self.assertRaises(TypeError, Interest().compound_interest, 'init amt', 1, 2)
        self.assertRaises(TypeError, Interest().compound_interest, 100, 'rate', 1, 2)
        self.assertRaises(TypeError, Interest().compound_interest, 100, .5, 'time', 2)
        self.assertRaises(TypeError, Interest().compound_interest, 100, .5, 1, 'compound num')


        self.assertRaises(TypeError, Interest().compound_interest, True, .5, 1, 2)
        self.assertRaises(TypeError, Interest().compound_interest, 100, True, 1, 2)
        self.assertRaises(TypeError, Interest().compound_interest, 100, .5, True, 2)
        self.assertRaises(TypeError, Interest().compound_interest, 100, .5, 1, True)

        self.assertRaises(TypeError, Interest().compound_interest, 1+3j, .5, 1, 2)    
        self.assertRaises(TypeError, Interest().compound_interest, 100, 1+3j, 1, 2)
        self.assertRaises(TypeError, Interest().compound_interest, 100, .5, 1+3j, 2)      
        self.assertRaises(TypeError, Interest().compound_interest, 100, .5, 1, 1+3j)


    def test_compound_interest_value_error(self):
        """ Test all arguments of the function to ensure that negatives, non decimals, and negative time durations dont work """
        self.assertRaises(ValueError, Interest().compound_interest, -100, .5, 1, 2) # Check negative principal val
        self.assertRaises(ValueError, Interest().compound_interest, 100, -.5, 1, 2) # Check negative rate val
        self.assertRaises(ValueError, Interest().compound_interest, 100, 1.5, 1, 2) # Check rate val over 1
        self.assertRaises(ValueError, Interest().compound_interest, 100, .5, -1, 2) # Check negative time val
        self.assertRaises(ValueError, Interest().compound_interest, 100, .5, 1, -2) # Check num times per year val less than 0

    
    def test_compound_output_correctness(self):
        """ Test and make sure the functions are outputting the expected values """
        self.assertAlmostEqual(Interest().compound_interest(100, .5, 1, 2), 100 * (1 + .5 / 2)**(2 * 1))
        self.assertAlmostEqual(Interest().compound_interest(0, .5, 1, 2), 0 * (1 + .5 / 2)**(2 * 1))
        self.assertAlmostEqual(Interest().compound_interest(17659, .03, 10, 2), 17659 * (1 + .03 / 2)**(2 * 10))
