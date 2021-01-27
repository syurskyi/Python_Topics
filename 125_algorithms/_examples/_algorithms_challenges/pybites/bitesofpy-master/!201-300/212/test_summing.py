import inspect

from summing import sum_numbers


def test_functionality():
    numbers = [1, 2, 0, 4, 5, 12, 'a', 3]
    actual = list(sum_numbers(numbers))
    expected = [0.5, 0.0, 0.8, 0.4166666666666667]
    a__ actual == expected


def test_use_of_idioms():
    src = inspect.getsource(sum_numbers)
    a__ 'try' not in src
    a__ 'except ' not in src
    a__ 'yield' in src
    a__ 'TypeError' in src
    a__ 'ZeroDivisionError' in src
    a__ src.count('suppress(') in (1, 2)
    a__ src.count('with') in (1, 2)