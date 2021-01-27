from itertools import islice

import pytest

from Previous.traffic import traffic_light, State


@pytest.fixture(scope="module")
def slice1():
    it = traffic_light()
    return list(islice(it, 96))


@pytest.fixture(scope="module")
def slice2():
    it = traffic_light()
    return list(islice(it, 100, 217))


def test_iterator_islice(slice1, slice2):
    a__ len(slice1) == 96
    a__ len(slice2) == 117

    a__ slice1[0] == State(color='red', command='Stop', timeout=2)
    a__ slice2[0] == State(color='green', command='Go', timeout=2)

    a__ slice1[-1] == State(color='amber', command='Caution', timeout=0.5)
    a__ slice2[-1] == State(color='red', command='Stop', timeout=2)


def test_equal_values_in_islice(slice1):
    for color in 'red green amber'.split():
        a__ sum(1 for state in slice1 if state.color == color) == 32


def test_return_types(slice2):
    a__ all(type(state) == State for state in slice2)


@pytest.mark.parametrize("color, expected", [
    ('red', 64),
    ('green', 64),
    ('amber', 16),
])
def test_timings(slice1, color, expected):
    timeout_for_color = sum(state.timeout for state in slice1
                            if state.color == color)
    a__ timeout_for_color == expected