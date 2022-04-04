"""Tests for the ocr-numbers exercise

Implementation note:
Both ocr.grid and ocr.number should validate their input
and raise ValueErrors with meaningful error messages
if necessary.
"""

_______ unittest

____ ocr _______ grid, number


c_ OcrTest(unittest.TestCase

    ___ test_0
        assertEqual('0', number([" _ ",
                                      "| |",
                                      "|_|",
                                      "   "]

    ___ test_1
        assertEqual('1', number(["   ",
                                      "  |",
                                      "  |",
                                      "   "]

    ___ test_garbage
        assertEqual('?', number([" _ ",
                                      " _|",
                                      "  |",
                                      "   "]

    ___ test_last_line_nonblank
        assertEqual('?', number(["   ",
                                      "  |",
                                      "  |",
                                      "| |"]

    ___ test_unknown_char
        assertEqual('?', number([" - ",
                                      " _|",
                                      " X|",
                                      "   "]

    ___ test_too_short_row
        assertRaises(V..., number, ["   ",
                                               " _|",
                                               " |",
                                               "   "])

    ___ test_insufficient_rows
        assertRaises(V..., number, ["   ",
                                               " _|",
                                               " X|"])

    ___ test_grid0
        assertEqual([" _ ",
                          "| |",
                          "|_|",
                          "   "], grid('0'

    ___ test_grid1
        assertEqual(["   ",
                          "  |",
                          "  |",
                          "   "], grid('1'

    ___ test_0010110
        assertEqual('0010110', number([" _  _     _        _ ",
                                            "| || |  || |  |  || |",
                                            "|_||_|  ||_|  |  ||_|",
                                            "                     "]

    ___ test_3186547290
        d.. = '3186547290'
        assertEqual(d.., number([" _     _  _  _     _  _  _  _ ",
                                         " _|  ||_||_ |_ |_|  | _||_|| |",
                                         " _|  ||_||_| _|  |  ||_  _||_|",
                                         "                              "]

    ___ test_Lost
        d.. = '4815162342'
        assertEqual(d.., number(["    _     _     _  _  _     _ ",
                                         "|_||_|  ||_   ||_  _| _||_| _|",
                                         "  ||_|  | _|  ||_||_  _|  ||_ ",
                                         "                              "]

    ___ test_garble_middle
        assertEqual('12?45', number(["    _  _     _ ",
                                          "  | _|  ||_||_ ",
                                          "  ||_  _|  | _|",
                                          "               "]

    ___ test_grid3186547290
        d.. = '3186547290'
        assertEqual([" _     _  _  _     _  _  _  _ ",
                          " _|  ||_||_ |_ |_|  | _||_|| |",
                          " _|  ||_||_| _|  |  ||_  _||_|",
                          "                              "], grid(d..

    ___ test_invalid_grid
        assertRaises(V..., grid, '123a')


__ _____ __ _____
    unittest.main()
