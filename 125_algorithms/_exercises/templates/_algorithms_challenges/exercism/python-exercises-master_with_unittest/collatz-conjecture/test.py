_______ unittest

____ collatz_conjecture _______ collatz_steps

# Test cases adapted from `x-common//canonical-data.json` @ version: 1.1.1


c_ CollatzConjectureTests(unittest.TestCase):

    ___ test_zero_steps_for_one
        assertEqual(collatz_steps(1), 0)

    ___ test_divide_if_even
        assertEqual(collatz_steps(16), 4)

    ___ test_even_and_odd_steps
        assertEqual(collatz_steps(12), 9)

    ___ test_large_number_of_even_and_odd_steps
        assertEqual(collatz_steps(1000000), 152)

    ___ test_zero_is_invalid_input
        assertEqual(collatz_steps(0), N..)

    ___ test_negative_number_is_invalid_input
        assertEqual(collatz_steps(-1), N..)

        assertEqual(collatz_steps(-15), N..)


__ __name__ __ '__main__':
    unittest.main()
