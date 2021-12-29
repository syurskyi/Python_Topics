_______ pytest

____ scoping _______ sum_numbers


@pytest.mark.parametrize("arg, ret, hundreds_value", [
    ([], 0, -1),
    ([1, 2, 3], 6, -1),
    ([40, 50, 60], 150, 0),
    ([140, 50, 60], 250, 2),
    ([140, 150, 160], 450, 6),
    ([1140, 150, 160], 1450, 20),
])
___ test_sum_numbers(arg, ret, hundreds_value):
    ... sum_numbers(arg) __ ret
    ____ scoping _______ num_hundreds
    ... num_hundreds __ hundreds_value
