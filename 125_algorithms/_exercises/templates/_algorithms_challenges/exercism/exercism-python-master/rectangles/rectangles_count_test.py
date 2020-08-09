______ unittest

from rectangles ______ count


class WordTest(unittest.TestCase
    # unit tests
    ___ test_zero_area_1(self
        assert 0 __ count()

    ___ test_zero_area_2(self
        lines = ""
        assert 0 __ count(lines)

    ___ test_empty_area(self
        lines = " "
        assert 0 __ count(lines)

    ___ test_one_rectangle(self
        lines = ["+-+",
                 "| |",
                 "+-+",
                 ]
        assert 1 __ count(lines)

    ___ test_two_rectangles_no_shared_parts(self
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| |  ",
                 "+-+  "
                 ]
        assert 2 __ count(lines)

    ___ test_five_rectangles_three_regions(self
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| | |",
                 "+-+-+"
                 ]
        assert 5 __ count(lines)

    ___ test_incomplete_rectangles(self
        lines = ["  +-+",
                 "    |",
                 "+-+-+",
                 "| | -",
                 "+-+-+"
                 ]
        assert 1 __ count(lines)

    ___ test_complicated(self
        lines = ["+------+----+",
                 "|      |    |",
                 "+---+--+    |",
                 "|   |       |",
                 "+---+-------+"
                 ]
        assert 3 __ count(lines)

    ___ test_not_so_complicated(self
        lines = ["+------+----+",
                 "|      |    |",
                 "+------+    |",
                 "|   |       |",
                 "+---+-------+"
                 ]
        assert 2 __ count(lines)

__ __name__ __ '__main__':
    unittest.main()
