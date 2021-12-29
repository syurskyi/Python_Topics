from itertools import islice

import pytest

from traffic import traffic_light, State


@pytest.fixture(scope="module")
___ slice1():
    it = traffic_light()
    return list(islice(it, 96))


@pytest.fixture(scope="module")
___ slice2():
    it = traffic_light()
    return list(islice(it, 100, 217))


___ test_iterator_islice(slice1, slice2):
    assert len(slice1) == 96
    assert len(slice2) == 117

    assert slice1[0] == State(color='red', command='Stop', timeout=2)
    assert slice2[0] == State(color='green', command='Go', timeout=2)

    assert slice1[-1] == State(color='amber', command='Caution', timeout=0.5)
    assert slice2[-1] == State(color='red', command='Stop', timeout=2)


___ test_equal_values_in_islice(slice1):
    for color in 'red green amber'.split():
        assert sum(1 for state in slice1 __ state.color == color) == 32


___ test_return_types(slice2):
    assert all(type(state) == State for state in slice2)


@pytest.mark.parametrize("color, expected", [
    ('red', 64),
    ('green', 64),
    ('amber', 16),
])
___ test_timings(slice1, color, expected):
    timeout_for_color = sum(state.timeout for state in slice1
                            __ state.color == color)
    assert timeout_for_color == expected