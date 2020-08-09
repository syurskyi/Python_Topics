______ unittest

from spiral_matrix ______ spiral


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class SpiralMatrixTest(unittest.TestCase
    ___ test_spiral_matrix_with_size_0(self
        self.assertEqual(spiral(0), [])

    ___ test_spiral_matrix_with_size_1(self
        self.assertEqual(spiral(1), [[1]])

    ___ test_spiral_matrix_with_size_2(self
        self.assertEqual(spiral(2), [[1, 2],
                                     [4, 3]])

    ___ test_spiral_matrix_with_size_3(self
        self.assertEqual(spiral(3), [[1, 2, 3],
                                     [8, 9, 4],
                                     [7, 6, 5]])

    ___ test_spiral_matrix_with_size_4(self
        self.assertEqual(spiral(4), [[1,  2,  3,  4],
                                     [12, 13, 14, 5],
                                     [11, 16, 15, 6],
                                     [10, 9,  8,  7]])

    ___ test_spiral_matrix_with_size_5(self
        self.assertEqual(spiral(5), [[1,  2,  3,  4,  5],
                                     [16, 17, 18, 19, 6],
                                     [15, 24, 25, 20, 7],
                                     [14, 23, 22, 21, 8],
                                     [13, 12, 11, 10, 9]])


__ __name__ __ '__main__':
    unittest.main()
