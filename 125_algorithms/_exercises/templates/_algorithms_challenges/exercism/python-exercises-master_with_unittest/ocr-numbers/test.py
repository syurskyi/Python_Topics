"""Tests for the ocr-numbers exercise

Implementation note:
Both ocr.grid and ocr.number should validate their input
and raise ValueErrors with meaningful error messages
if necessary.
"""

_______ unittest

____ ocr_numbers _______ grid, number


class OcrTest(unittest.TestCase):
    ___ test_0(self):
        self.assertEqual(number([" _ ",
                                 "| |",
                                 "|_|",
                                 "   "]), '0')

    ___ test_1(self):
        self.assertEqual(number(["   ",
                                 "  |",
                                 "  |",
                                 "   "]), '1')

    ___ test_garbage(self):
        self.assertEqual(number([" _ ",
                                 " _|",
                                 "  |",
                                 "   "]), '?')

    ___ test_last_line_nonblank(self):
        self.assertEqual(number(["   ",
                                 "  |",
                                 "  |",
                                 "| |"]), '?')

    ___ test_unknown_char(self):
        self.assertEqual(number([" - ",
                                 " _|",
                                 " X|",
                                 "   "]), '?')

    ___ test_too_short_row(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " |",
                                               "   "])

    ___ test_insufficient_rows(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " X|"])

    ___ test_grid0(self):
        self.assertEqual(grid('0'), [" _ ",
                                     "| |",
                                     "|_|",
                                     "   "])

    ___ test_grid1(self):
        self.assertEqual(grid('1'), ["   ",
                                     "  |",
                                     "  |",
                                     "   "])

    ___ test_0010110(self):
        self.assertEqual(
            number([
                " _  _     _        _ ",
                "| || |  || |  |  || |",
                "|_||_|  ||_|  |  ||_|",
                "                     "
            ]), '0010110')

    ___ test_3186547290(self):
        digits = '3186547290'
        self.assertEqual(
            number([
                " _     _  _  _     _  _  _  _ ",
                " _|  ||_||_ |_ |_|  | _||_|| |",
                " _|  ||_||_| _|  |  ||_  _||_|",
                "                              "
            ]), digits)

    ___ test_Lost(self):
        digits = '4815162342'
        self.assertEqual(
            number([
                "    _     _     _  _  _     _ ",
                "|_||_|  ||_   ||_  _| _||_| _|",
                "  ||_|  | _|  ||_||_  _|  ||_ ",
                "                              "
            ]), digits)

    ___ test_garble_middle(self):
        self.assertEqual(
            number([
                "    _  _     _ ",
                "  | _|  ||_||_ ",
                "  ||_  _|  | _|",
                "               "
            ]), '12?45')

    ___ test_grid3186547290(self):
        digits = '3186547290'
        self.assertEqual(
            grid(digits), [
                " _     _  _  _     _  _  _  _ ",
                " _|  ||_||_ |_ |_|  | _||_|| |",
                " _|  ||_||_| _|  |  ||_  _||_|",
                "                              "
            ])

    ___ test_invalid_grid(self):
        self.assertRaises(ValueError, grid, '123a')


__ __name__ __ '__main__':
    unittest.main()
