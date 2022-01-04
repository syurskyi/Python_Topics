"""Tests for the ocr-numbers exercise

Implementation note:
Both ocr.grid and ocr.number should validate their input
and raise ValueErrors with meaningful error messages
if necessary.
"""

_______ unittest

____ ocr_numbers _______ grid, number


c_ OcrTest(unittest.TestCase):
    ___ test_0
        assertEqual(number([" _ ",
                                 "| |",
                                 "|_|",
                                 "   "]), '0')

    ___ test_1
        assertEqual(number(["   ",
                                 "  |",
                                 "  |",
                                 "   "]), '1')

    ___ test_garbage
        assertEqual(number([" _ ",
                                 " _|",
                                 "  |",
                                 "   "]), '?')

    ___ test_last_line_nonblank
        assertEqual(number(["   ",
                                 "  |",
                                 "  |",
                                 "| |"]), '?')

    ___ test_unknown_char
        assertEqual(number([" - ",
                                 " _|",
                                 " X|",
                                 "   "]), '?')

    ___ test_too_short_row
        assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " |",
                                               "   "])

    ___ test_insufficient_rows
        assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " X|"])

    ___ test_grid0
        assertEqual(grid('0'), [" _ ",
                                     "| |",
                                     "|_|",
                                     "   "])

    ___ test_grid1
        assertEqual(grid('1'), ["   ",
                                     "  |",
                                     "  |",
                                     "   "])

    ___ test_0010110
        assertEqual(
            number([
                " _  _     _        _ ",
                "| || |  || |  |  || |",
                "|_||_|  ||_|  |  ||_|",
                "                     "
            ]), '0010110')

    ___ test_3186547290
        d.. = '3186547290'
        assertEqual(
            number([
                " _     _  _  _     _  _  _  _ ",
                " _|  ||_||_ |_ |_|  | _||_|| |",
                " _|  ||_||_| _|  |  ||_  _||_|",
                "                              "
            ]), d..)

    ___ test_Lost
        d.. = '4815162342'
        assertEqual(
            number([
                "    _     _     _  _  _     _ ",
                "|_||_|  ||_   ||_  _| _||_| _|",
                "  ||_|  | _|  ||_||_  _|  ||_ ",
                "                              "
            ]), d..)

    ___ test_garble_middle
        assertEqual(
            number([
                "    _  _     _ ",
                "  | _|  ||_||_ ",
                "  ||_  _|  | _|",
                "               "
            ]), '12?45')

    ___ test_grid3186547290
        d.. = '3186547290'
        assertEqual(
            grid(d..), [
                " _     _  _  _     _  _  _  _ ",
                " _|  ||_||_ |_ |_|  | _||_|| |",
                " _|  ||_||_| _|  |  ||_  _||_|",
                "                              "
            ])

    ___ test_invalid_grid
        assertRaises(ValueError, grid, '123a')


__ __name__ __ '__main__':
    unittest.main()
