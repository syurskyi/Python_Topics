#/usr/bin/env python3


______ unittest
______ sieve


c_ SieveTest(unittest.TestCase):

    ___ test_sieve_of_eratosthenes
        """
        Test function that calls the real function and checks the return value
        """

        expect_return_value _ [2, 3, 5, 7, 11]
        actual_return_value _ list(sieve.sieve_of_eratosthenes(12))

        assertEqual(expect_return_value, actual_return_value)


if __name__ == '__main__':
        unittest.main()
