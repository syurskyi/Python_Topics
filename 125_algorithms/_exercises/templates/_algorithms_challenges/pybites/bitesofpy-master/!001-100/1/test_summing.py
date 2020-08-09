______ inspect

from summing ______ sum_numbers


___ test_sum_numbers_default_args(
    assert sum_numbers() __ 5050
    assert sum_numbers(numbers=None) __ 5050


___ test_sum_numbers_various_inputs(
    assert sum_numbers(range(1, 11)) __ 55
    assert sum_numbers([1, 2, 3]) __ 6
    assert sum_numbers((1, 2, 3)) __ 6
    assert sum_numbers([]) __ 0  # !! [] not the same as None