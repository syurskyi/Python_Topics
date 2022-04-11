_______ unittest
_______ go_counting


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

board5x5 [
    "  B  ",
    " B B ",
    "B W B",
    " W W ",
    "  W  "
]


c_ GoCountingTest(unittest.TestCase
    ___ test_black_corner_territory_on_5x5_board
        board go_counting.Board(board5x5)
        stone, territory board.territory(x=0, y=1)
        assertEqual(stone, go_counting.BLACK)
        assertSetEqual(territory, {(0, 0), (0, 1), (1, 0)})

    ___ test_white_center_territory_on_5x5_board
        board go_counting.Board(board5x5)
        stone, territory board.territory(x=2, y=3)
        assertEqual(stone, go_counting.WHITE)
        assertSetEqual(territory, {(2, 3)})

    ___ test_open_corner_territory_on_5x5_board
        board go_counting.Board(board5x5)
        stone, territory board.territory(x=1, y=4)
        assertEqual(stone, go_counting.NONE)
        assertSetEqual(territory, {(0, 3), (0, 4), (1, 4)})

    ___ test_a_stone_and_not_a_territory_on_5x5_board
        board go_counting.Board(board5x5)
        stone, territory board.territory(x=1, y=1)
        assertEqual(stone, go_counting.NONE)
        assertSetEqual(territory, s..

    ___ test_invalid_because_x_is_too_low
        board go_counting.Board(board5x5)
        w__ assertRaisesWithMessage(V...
            board.territory(x=-1, y=1)

    ___ test_invalid_because_x_is_too_high
        board go_counting.Board(board5x5)
        w__ assertRaisesWithMessage(V...
            board.territory(x=5, y=1)

    ___ test_invalid_because_y_is_too_low
        board go_counting.Board(board5x5)
        w__ assertRaisesWithMessage(V...
            board.territory(x=1, y=-1)

    ___ test_invalid_because_y_is_too_high
        board go_counting.Board(board5x5)
        w__ assertRaisesWithMessage(V...
            board.territory(x=1, y=5)

    ___ test_one_territory_is_the_whole_board
        board go_counting.Board([" "])
        territories board.territories()
        assertSetEqual(territories[go_counting.BLACK], s..
        assertSetEqual(territories[go_counting.WHITE], s..
        assertSetEqual(territories[go_counting.NONE], {(0, 0)})

    ___ test_two_territories_rectangular_board
        input_board [
            " BW ",
            " BW "
        ]
        board go_counting.Board(input_board)
        territories board.territories()
        assertSetEqual(territories[go_counting.BLACK], {(0, 0), (0, 1)})
        assertSetEqual(territories[go_counting.WHITE], {(3, 0), (3, 1)})
        assertSetEqual(territories[go_counting.NONE], s..

    ___ test_two_region_rectangular_board
        input_board [" B "]
        board go_counting.Board(input_board)
        territories board.territories()
        assertSetEqual(territories[go_counting.BLACK], {(0, 0), (2, 0)})
        assertSetEqual(territories[go_counting.WHITE], s..
        assertSetEqual(territories[go_counting.NONE], s..

    # Utility functions
    ___ setUp
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex assertRaisesRegexp

    ___ assertRaisesWithMessage  exception
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
