_______ unittest

____ word_search _______ WordSearch, Point


c_ WordSearchTests(unittest.TestCase

    @classmethod
    ___ setUpClass
        puzzle = ('jefblpepre\n'
                  'camdcimgtc\n'
                  'oivokprjsm\n'
                  'pbwasqroua\n'
                  'rixilelhrs\n'
                  'wolcqlirpc\n'
                  'screeaumgr\n'
                  'alxhpburyi\n'
                  'jalaycalmp\n'
                  'clojurermt')
        example = WordSearch(puzzle)

    ___ test_horizontal_words_left_to_right
        assertEqual(
            example.s..('clojure'),
            (Point(0, 9), Point(6, 9))
        )

    ___ test_horizontal_words_right_to_left
        assertEqual(
            example.s..('elixir'),
            (Point(5, 4), Point(0, 4))
        )

    ___ test_vertical_words_top_to_bottom
        assertEqual(
            example.s..('ecmascript'),
            (Point(9, 0), Point(9, 9))
        )

    ___ test_vertical_words_bottom_to_top
        assertEqual(
            example.s..('rust'),
            (Point(8, 4), Point(8, 1))
        )

    ___ test_diagonal_words_top_left_to_bottom_right
        assertEqual(
            example.s..('java'),
            (Point(0, 0), Point(3, 3))
        )

    ___ test_diagonal_upper_bottom_right_to_top_left
        assertEqual(
            example.s..('lua'),
            (Point(7, 8), Point(5, 6))
        )

    ___ test_diagonal_upper_bottom_left_to_top_right
        assertEqual(
            example.s..('lisp'),
            (Point(2, 5), Point(5, 2))
        )

    ___ test_diagonal_upper_top_right_to_bottom_left
        assertEqual(
            example.s..('ruby'),
            (Point(7, 5), Point(4, 8))
        )

    ___ test_words_that_are_not_in_the_puzzle
        assertIsNone(example.s..('haskell'))

    ___ test_search_differently_sized_puzzles
        puzzle = ('qwertyuiopz\n'
                  'luamsicrexe\n'
                  'abcdefghijk')
        assertEqual(
            WordSearch(puzzle).s..('exercism'),
            (Point(10, 1), Point(3, 1))
        )


__ _____ __ _____
    unittest.main()
