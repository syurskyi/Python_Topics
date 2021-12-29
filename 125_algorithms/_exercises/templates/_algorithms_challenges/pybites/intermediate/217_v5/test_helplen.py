_______ i___

_______ pytest

____ Previous.helplen _______ get_len_help_text


___ test_pow():
    ... get_len_help_text(pow) __ 278


___ test_max():
    ... get_len_help_text(max) __ 402


___ test_bad_input():
    max1 = object()
    with pytest.raises(ValueError):
        get_len_help_text(max1)


___ test_another_bad_input():
    with pytest.raises(ValueError):
        get_len_help_text('string')


___ test_src():
    src = i___.getsource(get_len_help_text)
    ... 'help' __ src
    ... 'redirect_stdout' __ src