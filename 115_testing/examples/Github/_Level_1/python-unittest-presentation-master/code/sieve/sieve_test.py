#/usr/bin/env python3


import unittest
import sieve


class SieveTest(unittest.TestCase):

    def test_sieve_of_eratosthenes(self):
        """
        Test function that calls the real function and checks the return value
        """

        expect_return_value = [2, 3, 5, 7, 11]
        actual_return_value = list(sieve.sieve_of_eratosthenes(12))

        self.assertEqual(expect_return_value, actual_return_value)


if __name__ == '__main__':
        unittest.main()
