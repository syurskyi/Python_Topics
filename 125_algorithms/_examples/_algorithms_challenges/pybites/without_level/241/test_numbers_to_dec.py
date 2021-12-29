import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize('test_input',
                         [(['1', 2, 3, 4, 5]),
                          ([True, 1, 2, 3, 4])])
def test_type_error(test_input):
    with pytest.raises(TypeError):
        list_to_decimal(test_input)


@pytest.mark.parametrize('test_input',
                         [(0, 2, 10),
                          (-1, 2, 9)])
def test_value_error(test_input):
    with pytest.raises(ValueError):
        list_to_decimal(test_input)


@pytest.mark.parametrize('test_input,expected',
                         [([0, 1, 2, 3], 123), ([1, 2, 3, 4, 5], 12345)])
def test_return_value(test_input, expected):
    assert list_to_decimal(test_input) == expected
