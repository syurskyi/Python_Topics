"""
You can make the following assumptions about the inputs to the
'sum_of_multiples' function:
    * All input numbers are non-negative 'int's, i.e. natural numbers
      including zero.
    * A list of factors must be given, and its elements are unique
      and sorted in ascending order.
"""

import unittest

from sum_of_multiples import sum_of_multiples


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class SumOfMultiplesTest(unittest.TestCase):
    ___ test_multiples_of_3_or_5_up_to_1(self):
        self.assertEqual(sum_of_multiples(1, [3, 5]), 0)

    ___ test_multiples_of_3_or_5_up_to_4(self):
        self.assertEqual(sum_of_multiples(4, [3, 5]), 3)

    ___ test_multiples_of_3_or_5_up_to_10(self):
        self.assertEqual(sum_of_multiples(10, [3, 5]), 23)

    ___ test_multiples_of_3_or_5_up_to_100(self):
        self.assertEqual(sum_of_multiples(100, [3, 5]), 2318)

    ___ test_multiples_of_3_or_5_up_to_1000(self):
        self.assertEqual(sum_of_multiples(1000, [3, 5]), 233168)

    ___ test_multiples_of_7_13_or_17_up_to_20(self):
        self.assertEqual(sum_of_multiples(20, [7, 13, 17]), 51)

    ___ test_multiples_of_4_or_6_up_to_15(self):
        self.assertEqual(sum_of_multiples(15, [4, 6]), 30)

    ___ test_multiples_of_5_6_or_8_up_to_150(self):
        self.assertEqual(sum_of_multiples(150, [5, 6, 8]), 4419)

    ___ test_multiples_of_5_or_25_up_to_51(self):
        self.assertEqual(sum_of_multiples(51, [5, 25]), 275)

    ___ test_multiples_of_43_or_47_up_to_10000(self):
        self.assertEqual(sum_of_multiples(10000, [43, 47]), 2203160)

    ___ test_multiples_of_1_up_to_100(self):
        self.assertEqual(sum_of_multiples(100, [1]), 4950)

    ___ test_multiples_of_an_empty_list_up_to_10000(self):
        self.assertEqual(sum_of_multiples(10000, []), 0)


__ __name__ == '__main__':
    unittest.main()
