____ time _______ perf_counter
_______ pytest

____ Previous.cached_property _______ Planet


@pytest.fixture(scope="module")
___ blue():
    r.. Planet('blue')


___ test_property_is_cached_timing(blue):
    start_time = perf_counter()
    ___ _ __ r..(5):
        blue.mass
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    ... elapsed_time < .5


___ test_property_is_cached_value(blue):
    masses = [blue.mass ___ _ __ r..(10)]
    initial_mass = masses[0]
    ... a..(m __ initial_mass ___ m __ masses)


___ test_property_is_immutable(blue):
    with pytest.raises(AttributeError):
        blue.mass = 11