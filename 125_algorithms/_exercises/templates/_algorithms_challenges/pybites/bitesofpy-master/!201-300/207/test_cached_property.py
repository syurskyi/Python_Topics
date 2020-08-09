from time ______ perf_counter
______ pytest

from Previous.cached_property ______ Planet


@pytest.fixture(scope="module")
___ blue(
    r_ Planet('blue')


___ test_property_is_cached_timing(blue
    start_time = perf_counter()
    ___ _ in range(5
        blue.mass
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    assert elapsed_time < .5


___ test_property_is_cached_value(blue
    masses = [blue.mass ___ _ in range(10)]
    initial_mass = masses[0]
    assert all(m __ initial_mass ___ m in masses)


___ test_property_is_immutable(blue
    with pytest.raises(AttributeError
        blue.mass = 11