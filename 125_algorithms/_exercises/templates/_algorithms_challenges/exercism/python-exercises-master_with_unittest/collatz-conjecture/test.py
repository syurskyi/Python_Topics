_______ unittest

____ collatz_conjecture _______ collatz_steps

# Test cases adapted from `x-common//canonical-data.json` @ version: 1.1.1


class CollatzConjectureTests(unittest.TestCase):

    ___ test_zero_steps_for_one(self):
        self.assertEqual(collatz_steps(1), 0)

    ___ test_divide_if_even(self):
        self.assertEqual(collatz_steps(16), 4)

    ___ test_even_and_odd_steps(self):
        self.assertEqual(collatz_steps(12), 9)

    ___ test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(collatz_steps(1000000), 152)

    ___ test_zero_is_invalid_input(self):
        self.assertEqual(collatz_steps(0), N..)

    ___ test_negative_number_is_invalid_input(self):
        self.assertEqual(collatz_steps(-1), N..)

        self.assertEqual(collatz_steps(-15), N..)


__ __name__ __ '__main__':
    unittest.main()
