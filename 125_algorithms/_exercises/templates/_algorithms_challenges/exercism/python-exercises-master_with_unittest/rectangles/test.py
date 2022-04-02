_______ unittest

____ rectangles _______ count


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ WordTest(unittest.TestCase
    ___ test_no_rows
        assertEqual(c.. []), 0)

    ___ test_no_columns
        assertEqual(c.. ['']), 0)

    ___ test_no_rectangles
        assertEqual(c..  ' ' ), 0)

    ___ test_one_rectangle
        lines =  '+-+',
                 '| |',
                 '+-+'
        assertEqual(c.. lines), 1)

    ___ test_two_rectangles_without_shared_parts
        lines =  '  +-+',
                 '  | |',
                 '+-+-+',
                 '| |  ',
                 '+-+  '
        assertEqual(c.. lines), 2)

    ___ test_five_rectangles_with_shared_parts
        lines =  '  +-+',
                 '  | |',
                 '+-+-+',
                 '| | |',
                 '+-+-+'
        assertEqual(c.. lines), 5)

    ___ test_rectangle_of_height_1_is_counted
        lines =  '+--+',
                 '+--+'
        assertEqual(c.. lines), 1)

    ___ test_rectangle_of_width_1_is_counted
        lines =  '++',
                 '||',
                 '++'
        assertEqual(c.. lines), 1)

    ___ test_1x1_square_is_counted
        lines =  '++',
                 '++'
        assertEqual(c.. lines), 1)

    ___ test_only_complete_rectangles_are_counted
        lines =  '  +-+',
                 '    |',
                 '+-+-+',
                 '| | -',
                 '+-+-+'
        assertEqual(c.. lines), 1)

    ___ test_rectangles_can_be_of_different_sizes
        lines =  '+------+----+',
                 '|      |    |',
                 '+---+--+    |',
                 '|   |       |',
                 '+---+-------+'
        assertEqual(c.. lines), 3)

    ___ test_corner_is_required_for_a_rectangle_to_be_complete
        lines =  '+------+----+',
                 '|      |    |',
                 '+------+    |',
                 '|   |       |',
                 '+---+-------+'
        assertEqual(c.. lines), 2)

    ___ test_large_input_with_many_rectangles
        lines =  '+---+--+----+',
                 '|   +--+----+',
                 '+---+--+    |',
                 '|   +--+----+',
                 '+---+--+--+-+',
                 '+---+--+--+-+',
                 '+------+  | |',
                 '          +-+'
        assertEqual(c.. lines), 60)


__ _____ __ _____
    unittest.main()
