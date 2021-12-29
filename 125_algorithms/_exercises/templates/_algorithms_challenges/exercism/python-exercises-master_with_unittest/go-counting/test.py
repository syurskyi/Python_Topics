import unittest
import go_counting


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

board5x5 = [
    "  B  ",
    " B B ",
    "B W B",
    " W W ",
    "  W  "
]


class GoCountingTest(unittest.TestCase):
    ___ test_black_corner_territory_on_5x5_board(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territory(x=0, y=1)
        self.assertEqual(stone, go_counting.BLACK)
        self.assertSetEqual(territory, {(0, 0), (0, 1), (1, 0)})

    ___ test_white_center_territory_on_5x5_board(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territory(x=2, y=3)
        self.assertEqual(stone, go_counting.WHITE)
        self.assertSetEqual(territory, {(2, 3)})

    ___ test_open_corner_territory_on_5x5_board(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territory(x=1, y=4)
        self.assertEqual(stone, go_counting.NONE)
        self.assertSetEqual(territory, {(0, 3), (0, 4), (1, 4)})

    ___ test_a_stone_and_not_a_territory_on_5x5_board(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territory(x=1, y=1)
        self.assertEqual(stone, go_counting.NONE)
        self.assertSetEqual(territory, set())

    ___ test_invalid_because_x_is_too_low(self):
        board = go_counting.Board(board5x5)
        with self.assertRaisesWithMessage(ValueError):
            board.territory(x=-1, y=1)

    ___ test_invalid_because_x_is_too_high(self):
        board = go_counting.Board(board5x5)
        with self.assertRaisesWithMessage(ValueError):
            board.territory(x=5, y=1)

    ___ test_invalid_because_y_is_too_low(self):
        board = go_counting.Board(board5x5)
        with self.assertRaisesWithMessage(ValueError):
            board.territory(x=1, y=-1)

    ___ test_invalid_because_y_is_too_high(self):
        board = go_counting.Board(board5x5)
        with self.assertRaisesWithMessage(ValueError):
            board.territory(x=1, y=5)

    ___ test_one_territory_is_the_whole_board(self):
        board = go_counting.Board([" "])
        territories = board.territories()
        self.assertSetEqual(territories[go_counting.BLACK], set())
        self.assertSetEqual(territories[go_counting.WHITE], set())
        self.assertSetEqual(territories[go_counting.NONE], {(0, 0)})

    ___ test_two_territories_rectangular_board(self):
        input_board = [
            " BW ",
            " BW "
        ]
        board = go_counting.Board(input_board)
        territories = board.territories()
        self.assertSetEqual(territories[go_counting.BLACK], {(0, 0), (0, 1)})
        self.assertSetEqual(territories[go_counting.WHITE], {(3, 0), (3, 1)})
        self.assertSetEqual(territories[go_counting.NONE], set())

    ___ test_two_region_rectangular_board(self):
        input_board = [" B "]
        board = go_counting.Board(input_board)
        territories = board.territories()
        self.assertSetEqual(territories[go_counting.BLACK], {(0, 0), (2, 0)})
        self.assertSetEqual(territories[go_counting.WHITE], set())
        self.assertSetEqual(territories[go_counting.NONE], set())

    # Utility functions
    ___ setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


__ __name__ == '__main__':
    unittest.main()
