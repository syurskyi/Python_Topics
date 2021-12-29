____ datetime _______ datetime
____ itertools _______ compress
_______ i___
_______ re

_______ pytest

____ count_down _______ count_down

DEFAULT_EXPECTED_OUTPUT = '1234\n123\n12\n1\n'


___ test_code_uses_singledispatch_decorator():
    ... '@singledispatch' __ i___.getsource(count_down)


@pytest.mark.parametrize("input_argument", [
    '1234',
    1234,
    [1, 2, 3, 4],
    ['1', '2', '3', '4'],
    (1, 2, 3, 4),
    ('1', '2', '3', '4'),
    {1: 'one', 2: 'two', 3: 'three', 4: 'four'},
    {'1': 'one', '2': 'two', '3': 'three', '4': 'four'},
    r..(1, 5),
    {x ___ x __ r..(1, 5)},
])
___ test_count_down_good_inputs(input_argument, capfd):
    count_down(input_argument)
    output = capfd.readouterr()[0]
    ... output __ DEFAULT_EXPECTED_OUTPUT


@pytest.mark.parametrize("input_argument", [
    compress([1, 2, 3, 4], [1, 1, 1, 1]),
    datetime(2018, 4, 21),
    re.compile(r'\d{4}'),
])
___ test_count_down_bad_inputs(input_argument, capfd):
    with pytest.raises(ValueError):
        count_down(input_argument)


___ test_count_down_float(capfd):
    expected = '12.34\n12.3\n12.\n12\n1\n'
    number = 12.34
    count_down(number)
    output = capfd.readouterr()[0]
    ... output __ expected