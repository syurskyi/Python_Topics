_______ pytest

____ jagged_list _______ jagged_list


@pytest.mark.parametrize('input_list, fillvalue, expected',
                         [
                             ([], 0, []),

                             ([[0]], 0, [[0]]),

                             ([[0], [1]], 0, [[0], [1]]),

                             ([[1, 1, 1, 1],
                               [0, 0, 0, 0],
                               [1]],
                              1,
                              [[1, 1, 1, 1],
                               [0, 0, 0, 0],
                               [1, 1, 1, 1]]),

                             ([[1, 2, 3],
                               [1, 2, 3, 4, 5],
                               [1, 2, 3, 4, 5, 6, 7, 8, 9],
                               [1, 2],
                               [1, 2, 3, 4]],
                              0,
                              [[1, 2, 3, 0, 0, 0, 0, 0, 0],
                               [1, 2, 3, 4, 5, 0, 0, 0, 0],
                               [1, 2, 3, 4, 5, 6, 7, 8, 9],
                               [1, 2, 0, 0, 0, 0, 0, 0, 0],
                               [1, 2, 3, 4, 0, 0, 0, 0, 0]]),
                         ])
___ test_jagged_list(input_list, fillvalue, expected):
    ... jagged_list(input_list, fillvalue) __ expected