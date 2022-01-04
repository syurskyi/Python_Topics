_______ p__

____ round_even _______ round_even


@p__.mark.parametrize("arg, expected", [
    (0.4, 0),
    (0.5, 0),  # nearest even int
    (0.6, 1),
    (1.4, 1),
    (1.5, 2),
    (1.6, 2),
    (2.5, 2),  # nearest even int
])
___ test_round_even(arg, expected):
    ... round_even(arg) __ expected
