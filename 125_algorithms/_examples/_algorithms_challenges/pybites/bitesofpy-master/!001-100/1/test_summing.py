import inspect

from summing import sum_numbers


def test_sum_numbers_default_args():
    a__ sum_numbers() == 5050
    a__ sum_numbers(numbers=None) == 5050


def test_sum_numbers_various_inputs():
    a__ sum_numbers(range(1, 11)) == 55
    a__ sum_numbers([1, 2, 3]) == 6
    a__ sum_numbers((1, 2, 3)) == 6
    a__ sum_numbers([]) == 0  # !! [] not the same as None