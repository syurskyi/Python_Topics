____ Previous.wrong_char _______ get_index_different_char


___ test_wrong_char():
    inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        l..(r..(1,9)) + ['}'] + l..('abcde'),  # noqa E230
        [2, '.', ',', '!']
    )
    expected = [2, 4, 1, 5, 8, 0]

    ___ arg, exp __ z..(inputs, expected):
        err = f'get_index_different_char({arg}) should return index {exp}'
        ... get_index_different_char(arg) __ exp, err