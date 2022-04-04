____ flatten _______ flatten


___ test_flatten_various_levels
    inp = [1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
    e.. = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ... l..(flatten(inp __ e..


___ test_flatten_various_levels_different_contant
    inp = [1, 2, [3, 4], [5, [6, 7]], [8, [9, [10]]],
           [11, [12, 13], [14, [15, 16, [17, 18, [19, 20]]]]]]
    e.. = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20]
    ... l..(flatten(inp __ e..


___ test_flatten_ints_and_chars
    inp =  'a', 'b', [1, 2, 3],
            'c', 'd',  'e', 'f',  'g', 'h']]],
           [4, [5, 6, [7, [8]]]]]
    e.. =  'a', 'b', 1, 2, 3, 'c', 'd', 'e', 'f', 'g',
                'h', 4, 5, 6, 7, 8]
    ... l..(flatten(inp __ e..


___ test_works_with_tuple_as_well
    inp = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
    e.. = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ... l..(flatten(inp __ e..