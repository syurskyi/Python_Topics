_______ pytest

____ numbers_to_dec _______ list_to_decimal


@pytest.mark.parametrize("good_seq, expected_result", [
    ([0, 2, 4, 8], 248),
    ([1, 0, 2], 102)
])
___ test_numbers_to_dec(good_seq, expected_result):
    ... list_to_decimal(good_seq) __ expected_result


@pytest.mark.parametrize("bad_seq", [
    [-3, 23],
    [5, 10]
])
___ test_numbers_to_dec_ValueError(bad_seq):
    with pytest.raises(ValueError):
        list_to_decimal(bad_seq)


@pytest.mark.parametrize("bad_seq", [
    [3.6, 23, 1],
    [1, '2', 3],
    ['3', '6', N..]
])
___ test_numbers_to_dec_TypeError(bad_seq):
    with pytest.raises(TypeError):
        list_to_decimal(bad_seq)
