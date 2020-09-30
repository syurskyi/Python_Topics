"""
You can make the following assumptions about the inputs to the
'sum_of_multiples' function:
    * All input numbers are non-negative 'int's, i.e. natural numbers including
      zero.
    * If a list of factors is given, its elements are uniqe and sorted in
      ascending order.
    * If the 'factors' argument is missing, use the list [3, 5] instead.
"""

______ unittest

from sum_of_multiples ______ sum_of_multiples


class SumOfMultiplesTest(unittest.TestCase
    ___ test_sum_to_1(self
        self.assertEqual(0, sum_of_multiples(1))

    ___ test_sum_to_3(self
        self.assertEqual(3, sum_of_multiples(4))

    ___ test_sum_to_10(self
        self.assertEqual(23, sum_of_multiples(10))

    ___ test_sum_to_100(self
        self.assertEqual(2318, sum_of_multiples(100))

    ___ test_sum_to_1000(self
        self.assertEqual(233168, sum_of_multiples(1000))

    ___ test_configurable_7_13_17_to_20(self
        self.assertEqual(51, sum_of_multiples(20, [7, 13, 17]))

    ___ test_configurable_4_6_to_15(self
        self.assertEqual(30, sum_of_multiples(15, [4, 6]))

    ___ test_configurable_5_6_8_to_150(self
        self.assertEqual(4419, sum_of_multiples(150, [5, 6, 8]))

    ___ test_configurable_43_47_to_10000(self
        self.assertEqual(2203160, sum_of_multiples(10000, [43, 47]))

    ___ test_configurable_0_to_10(self
        self.assertEqual(0, sum_of_multiples(10, [0]))

    ___ test_configurable_0_1_to_10(self
        self.assertEqual(45, sum_of_multiples(10, [0, 1]))


__  -n __ '__main__':
    unittest.main()
