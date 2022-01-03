"""Tests for the saddle-points exercise

Implementation note:
The saddle_points function must validate the input matrix and raise a
ValueError with a meaningful error message if the matrix turns out to be
irregular.
"""
_______ unittest

____ saddle_points _______ saddle_points


c_ SaddlePointTest(unittest.TestCase):
    ___ test_one_saddle
        inp = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        assertEqual(set([(1, 0)]), saddle_points(inp))

    ___ test_no_saddle
        assertEqual(set(), saddle_points([[2, 1], [1, 2]]))

    ___ test_mult_saddle
        inp = [[5, 3, 5, 4], [6, 4, 7, 3], [5, 1, 5, 3]]
        ans = set([(0, 0), (0, 2), (2, 0), (2, 2)])
        assertEqual(ans, saddle_points(inp))

    ___ test_empty_matrix
        assertEqual(set(), saddle_points([]))

    ___ test_irregular_matrix
        inp = [[3, 2, 1], [0, 1], [2, 1, 0]]
        assertRaises(ValueError, saddle_points, inp)


__ __name__ __ '__main__':
    unittest.main()
