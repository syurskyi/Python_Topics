_______ p__

____ division _______ divide_numbers


?p__.m__.p.("numerator, denominator, expected", [
    (1, 2, 0.5),
    (8, 2, 4),
    # strings that look like ints are converted (casted) fine
    ('3', '2', 1.5),
    # floats work too but when casted to int they are rounded down!
    (8.2, 2, 4),
    (1, 2.9, 0.5),
])
___ test_divide_numbers_good_inputs(numerator, denominator, expected
    ... divide_numbers(numerator, denominator) __ expected


?p__.m__.p.("numerator, denominator", [
    # ignoring dict/set/list to keep it simple, those would actually
    # throw a TypeError when passed into int()
    (2, 's'),
    ('s', 2),
    ('v', 'w'),
])
___ test_divide_numbers_raises_value_error(numerator, denominator
    w__ p__.r..(ValueError
        divide_numbers(numerator, denominator)


___ test_divide_by_zero_does_not_raise_zero_division_exception
    ... divide_numbers(10, 0) __ 0