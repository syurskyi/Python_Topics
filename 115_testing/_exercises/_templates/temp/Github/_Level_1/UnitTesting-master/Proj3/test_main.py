______ unittest
____ math ______ exp
____ main ______ Interest

c_ TestInterest(unittest.TestCase):
    ___ test_simple_interest_type_error
        """ Test all arguements of the function to determine that if rouge type is entered that it is caught """
        # Arrange (instantiate class)
        # Act (use instantiation)
        # Assert (assert method)
        assertRaises(TypeError, Interest().simple_interest, 'init amt', 1, 1)
        assertRaises(TypeError, Interest().simple_interest, True, .5, 1)
        assertRaises(TypeError, Interest().simple_interest, 1+3j, .5, 1)

        assertRaises(TypeError, Interest().simple_interest, 100, 'rate', 1)
        assertRaises(TypeError, Interest().simple_interest, 100, True, 1)
        assertRaises(TypeError, Interest().simple_interest, 100, 1+3j, 1)

        assertRaises(TypeError, Interest().simple_interest, 100, .5, 'time')
        assertRaises(TypeError, Interest().simple_interest, 100, .5, True)
        assertRaises(TypeError, Interest().simple_interest, 100, .5, 1+3j)

    ___ test_simple_interest_value_error
        """ Test all arguments of the function to ensure that negatives, non decimals, and negative time durations dont work """
        assertRaises(ValueError, Interest().simple_interest, -100, .5, 1)
        assertRaises(ValueError, Interest().simple_interest, 100, -.5, 1)
        assertRaises(ValueError, Interest().simple_interest, 100, .5, -1)
        assertRaises(ValueError, Interest().simple_interest, 100, 1.5, -1)
    
    ___ test_function_output_correctness
        """ Test and make sure the functions are outputting the expected values """
        assertAlmostEqual(Interest().simple_interest(100, .5, 1), 100 * (.5 * 1 + 1))
        assertAlmostEqual(Interest().simple_interest(0, .5, 1), 0 * (.5 * 1 + 1))
        assertAlmostEqual(Interest().simple_interest(17659, .03, 10), 17659 * (.03 * 10 + 1))

    ___ test_compound_interest_type_error
        """ Test all arguements of the function to determine that if rouge type is entered that it is caught """
        assertRaises(TypeError, Interest().compound_interest, 'init amt', 1, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, 'rate', 1, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, .5, 'time', 2)
        assertRaises(TypeError, Interest().compound_interest, 100, .5, 1, 'compound num')


        assertRaises(TypeError, Interest().compound_interest, True, .5, 1, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, True, 1, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, .5, True, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, .5, 1, True)

        assertRaises(TypeError, Interest().compound_interest, 1+3j, .5, 1, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, 1+3j, 1, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, .5, 1+3j, 2)
        assertRaises(TypeError, Interest().compound_interest, 100, .5, 1, 1+3j)


    ___ test_compound_interest_value_error
        """ Test all arguments of the function to ensure that negatives, non decimals, and negative time durations dont work """
        assertRaises(ValueError, Interest().compound_interest, -100, .5, 1, 2) # Check negative principal val
        assertRaises(ValueError, Interest().compound_interest, 100, -.5, 1, 2) # Check negative rate val
        assertRaises(ValueError, Interest().compound_interest, 100, 1.5, 1, 2) # Check rate val over 1
        assertRaises(ValueError, Interest().compound_interest, 100, .5, -1, 2) # Check negative time val
        assertRaises(ValueError, Interest().compound_interest, 100, .5, 1, -2) # Check num times per year val less than 0

    
    ___ test_compound_output_correctness
        """ Test and make sure the functions are outputting the expected values """
        assertAlmostEqual(Interest().compound_interest(100, .5, 1, 2), 100 * (1 + .5 / 2)**(2 * 1))
        assertAlmostEqual(Interest().compound_interest(0, .5, 1, 2), 0 * (1 + .5 / 2)**(2 * 1))
        assertAlmostEqual(Interest().compound_interest(17659, .03, 10, 2), 17659 * (1 + .03 / 2)**(2 * 10))
