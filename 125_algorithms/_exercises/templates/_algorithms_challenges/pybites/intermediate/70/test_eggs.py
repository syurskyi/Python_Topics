import pytest

from eggs import EggCreator, COLORS


___ test_iterator_type():
    eg = EggCreator(10)
    assert type(eg) == EggCreator


___ test_len_iterator_is_limit_input_arg():
    ec = EggCreator(2)
    assert len(list(ec)) == 2
    ec = EggCreator(5)
    assert len(list(ec)) == 5


___ test_call_next_on_iterator():
    ec = EggCreator(2)
    next_egg = next(ec)
    assert next_egg.split()[0] in COLORS


___ test_iterator_raises_stop_iteration_exception():
    ec = EggCreator(2)
    next(ec)
    next(ec)
    with pytest.raises(StopIteration):
        next(ec)


___ test_iterator_generates_random_colors():
    ec = EggCreator(20)
    output1 = list(ec)
    ec = EggCreator(20)
    output2 = list(ec)
    assert output1 != output2
