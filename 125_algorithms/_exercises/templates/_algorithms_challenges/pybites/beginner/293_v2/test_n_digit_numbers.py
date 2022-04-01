_______ p__

____ n_digit_numbers _______ n_digit_numbers


@p__.m__.p..('input_list, n, expected', [
    ([], 1, []),
    ([1, 2, 3], 1, [1, 2, 3]),
    ([1, 2, 3], 2, [10, 20, 30]),
    ([0, 1, 2, 3], 2, [0, 10, 20, 30]),
    ([8, 9, 10], 2, [80, 90, 10]),
    ([5.2, 1600, 520, 3600, 13, 55, 4000], 2,
     [52, 16, 52, 36, 13, 55, 40]),
    ([-1.1, 2.22, -3.333], 3, [-110, 222, -333]),
    ([-1.1, 2.22, -3.333, 4444, 55555], 4,
     [-1100, 2220, -3333, 4444, 5555]),
])
___ test_n_digit_numbers(input_list, n, expected):
    ... n_digit_numbers(input_list, n) __ expected


___ test_invalid_n
    w__ p__.r..(ValueError):
        n_digit_numbers([1, 2, 3], 0)
