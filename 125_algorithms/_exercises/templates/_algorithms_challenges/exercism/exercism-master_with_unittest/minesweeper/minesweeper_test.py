""" Tests for the minesweeper exercise

Implementation note:
The board function must validate its input and raise a
ValueError with a meaningfull error message if the
input turns out to be malformed.
"""

_______ unittest

____ minesweeper _______ board


c_ MinesweeperTest(unittest.TestCase):
    ___ test_board1
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
        assertEqual(out, board(inp))

    ___ test_board2
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
        assertEqual(out, board(inp))

    ___ test_board3
        inp = ["+-----+",
               "| * * |",
               "+-----+"]
        out = ["+-----+",
               "|1*2*1|",
               "+-----+"]
        assertEqual(out, board(inp))

    ___ test_board4
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
        assertEqual(out, board(inp))

    ___ test_board5
        inp = ["+-+",
               "|*|",
               "+-+"]
        out = ["+-+",
               "|*|",
               "+-+"]
        assertEqual(out, board(inp))

    ___ test_board6
        inp = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        out = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        assertEqual(out, board(inp))

    ___ test_board7
        inp = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        out = ["+--+",
               "|**|",
               "|**|",
               "+--+"]
        assertEqual(out, board(inp))

    ___ test_board8
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
        assertEqual(out, board(inp))

    ___ test_board9
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
        assertEqual(out, board(inp))

    ___ test_different_len
        inp = ["+-+",
               "| |",
               "|*  |",
               "|  |",
               "+-+"]
        assertRaises(ValueError, board, inp)

    ___ test_faulty_border
        inp = ["+-----+",
               "*   * |",
               "+-- --+"]
        assertRaises(ValueError, board, inp)

    ___ test_invalid_char
        inp = ["+-----+",
               "|X  * |",
               "+-----+"]
        assertRaises(ValueError, board, inp)


__ _____ __ _____
    unittest.main()
