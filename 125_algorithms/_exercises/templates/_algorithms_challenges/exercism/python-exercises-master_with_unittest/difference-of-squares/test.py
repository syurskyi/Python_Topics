_______ unittest

____ difference_of_squares _______ difference, square_of_sum, sum_of_squares


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

c_ DifferenceOfSquaresTest(unittest.TestCase):
    ___ test_square_of_sum_1
        assertEqual(square_of_sum(1), 1)

    ___ test_square_of_sum_5
        assertEqual(square_of_sum(5), 225)

    ___ test_square_of_sum_100
        assertEqual(square_of_sum(100), 25502500)

    ___ test_sum_of_squares_1
        assertEqual(sum_of_squares(1), 1)

    ___ test_sum_of_squares_5
        assertEqual(sum_of_squares(5), 55)

    ___ test_sum_of_squares_100
        assertEqual(sum_of_squares(100), 338350)

    ___ test_difference_of_squares_1
        assertEqual(difference(1), 0)

    ___ test_difference_of_squares_5
        assertEqual(difference(5), 170)

    ___ test_difference_of_squares_100
        assertEqual(difference(100), 25164150)


__ _____ __ _____
    unittest.main()
