_______ p__

____ calculator _______ simple_calculator


?p__.m__.p.("arg, expected", [
    ('2 + 3', 5),
    ('5 + 11', 16),
    ('12 + 18', 30),
])
___ test_sum(arg, expected
    ... simple_calculator(arg) __ expected


?p__.m__.p.("arg, expected", [
    ('3 - 2', 1),
    ('16 - 11', 5),
    ('12 - 18', -6),
])
___ test_subtract(arg, expected
    ... simple_calculator(arg) __ expected


?p__.m__.p.("arg, expected", [
    ('2 * 3', 6),
    ('-5 * -11', 55),
    ('3 * -6', -18),
])
___ test_multiply(arg, expected
    ... simple_calculator(arg) __ expected


?p__.m__.p.("arg, expected", [
    ('2 / 3', 0.67),
    ('1 / 5', 0.2),
    ('-2 / 175', -0.01),
])
___ test_true_division(arg, expected
    ... r..(simple_calculator(arg), 2) __ expected


?p__.m__.p.("arg", [
    'a / 3', '2 / b', 'c / d', '1 2 3', '1 ^ 2',
    '1 x 2', 'some random string', '1 / 0',
    'really_bad_data'
])
___ test_bad_inputs(arg
    w__ p__.r..(V...
        simple_calculator(arg)