import pytest

from calculator import simple_calculator


@pytest.mark.parametrize("arg, expected", [
    ('2 + 3', 5),
    ('5 + 11', 16),
    ('12 + 18', 30),
])
def test_sum(arg, expected):
    a__ simple_calculator(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ('3 - 2', 1),
    ('16 - 11', 5),
    ('12 - 18', -6),
])
def test_subtract(arg, expected):
    a__ simple_calculator(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ('2 * 3', 6),
    ('-5 * -11', 55),
    ('3 * -6', -18),
])
def test_multiply(arg, expected):
    a__ simple_calculator(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ('2 / 3', 0.67),
    ('1 / 5', 0.2),
    ('-2 / 175', -0.01),
])
def test_true_division(arg, expected):
    a__ round(simple_calculator(arg), 2) == expected


@pytest.mark.parametrize("arg", [
    'a / 3', '2 / b', 'c / d', '1 2 3', '1 ^ 2',
    '1 x 2', 'some random string', '1 / 0',
    'really_bad_data'
])
def test_bad_inputs(arg):
    with pytest.raises(ValueError):
        simple_calculator(arg)