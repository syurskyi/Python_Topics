_______ unittest

____ matrix _______ Matrix


c_ MatrixTest(unittest.TestCase
    ___ test_extract_a_row
        matrix = Matrix("1 2\n10 20")
        assertEqual(matrix.rows[0], [1, 2])

    ___ test_extract_same_row_again
        matrix = Matrix("9 7\n8 6")
        assertEqual(matrix.rows[0], [9, 7])

    ___ test_extract_other_row
        matrix = Matrix("9 8 7\n19 18 17")
        assertEqual(matrix.rows[1], [19, 18, 17])

    ___ test_extract_other_row_again
        matrix = Matrix("1 4 9\n16 25 36")
        assertEqual(matrix.rows[1], [16, 25, 36])

    ___ test_extract_a_column
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        assertEqual(matrix.columns[0], [1, 4, 7, 8])

    ___ test_extract_another_column
        matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
        assertEqual(matrix.columns[1], [1903, 3, 4])


__ _____ __ _____
    unittest.main()
