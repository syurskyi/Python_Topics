_______ unittest

____ difference_of_squares _______ difference, square_of_sum, sum_of_squares


c_ DifferenceOfSquaresTest(unittest.TestCase):

    ___ test_square_of_sum_5
        assertEqual(225, square_of_sum(5))

    ___ test_sum_of_squares_5
        assertEqual(55, sum_of_squares(5))

    ___ test_difference_5
        assertEqual(170, difference(5))

    ___ test_square_of_sum_100
        assertEqual(25502500, square_of_sum(100))

    ___ test_sum_of_squares_100
        assertEqual(338350, sum_of_squares(100))

    ___ test_difference_100
        assertEqual(25164150, difference(100))


__ __name__ __ '__main__':
    unittest.main()
