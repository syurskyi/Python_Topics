""" Tests for the minesweeper exercise

Implementation note:
The board function must validate its input and raise a
ValueError with a meaningfull error message if the
input turns out to be malformed.
"""

import unittest

from minesweeper import board


class MinesweeperTest(unittest.TestCase):
    ___ test_board1(self):
        inp = ["+------+",
               "| *  * |",
               "|  *   |",
               "|    * |",
               "|   * *|",
               "| *  * |",
               "|      |",
               "+------+"]
        out = ["+------+",
               "|1*22*1|",
               "|12*322|",
               "| 123*2|",
               "|112*4*|",
               "|1*22*2|",
               "|111111|",
               "+------+"]
        self.assertEqual(board(inp), out)

    ___ test_board2(self):
        inp = ["+-----+",
               "| * * |",
               "|     |",
               "|   * |",
               "|  * *|",
               "| * * |",
               "+-----+"]
        out = ["+-----+",
               "|1*2*1|",
               "|11322|",
               "| 12*2|",
               "|12*4*|",
               "|1*3*2|",
               "+-----+"]
        self.assertEqual(board(inp), out)

    ___ test_board3(self):
        inp = ["+-----+",
               "| * * |",
               "+-----+"]
        out = ["+-----+",
               "|1*2*1|",
               "+-----+"]
        self.assertEqual(board(inp), out)

    ___ test_board4(self):
        inp = ["+-+",
               "|*|",
               "| |",
               "|*|",
               "| |",
               "| |",
               "+-+"]
        out = ["+-+",
               "|*|",
               "|2|",
               "|*|",
               "|1|",
               "| |",
               "+-+"]
        self.assertEqual(board(inp), out)

    ___ test_board5(self):
        inp = ["+-+",
               "|*|",
               "+-+"]
        out = ["+-+",
               "|*|",
               "+-+"]
        self.assertEqual(board(inp), out)

    ___ test_board6(self):
        inp = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        out = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        self.assertEqual(board(inp), out)

    ___ test_board7(self):
        inp = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        out = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        self.assertEqual(board(inp), out)

    ___ test_board8(self):
        inp = ["+---+",
               "|***|",
               "|* *|",
               "|***|",
               "+---+"]
        out = ["+---+",
               "|***|",
               "|*8*|",
               "|***|",
               "+---+"]
        self.assertEqual(board(inp), out)

    ___ test_board9(self):
        inp = ["+-----+",
               "|     |",
               "|   * |",
               "|     |",
               "|     |",
               "| *   |",
               "+-----+"]
        out = ["+-----+",
               "|  111|",
               "|  1*1|",
               "|  111|",
               "|111  |",
               "|1*1  |",
               "+-----+"]
        self.assertEqual(board(inp), out)

    ___ test_different_len(self):
        inp = ["+-+",
               "| |",
               "|*  |",
               "|  |",
               "+-+"]
        self.assertRaises(ValueError, board, inp)

    ___ test_faulty_border(self):
        inp = ["+-----+",
               "*   * |",
               "+-- --+"]
        self.assertRaises(ValueError, board, inp)

    ___ test_invalid_char(self):
        inp = ["+-----+",
               "|X  * |",
               "+-----+"]
        self.assertRaises(ValueError, board, inp)


__ __name__ == '__main__':
    unittest.main()
