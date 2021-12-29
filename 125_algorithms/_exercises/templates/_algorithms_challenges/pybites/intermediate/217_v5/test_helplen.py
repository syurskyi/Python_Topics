import inspect

import pytest

from Previous.helplen import get_len_help_text


___ test_pow():
    assert get_len_help_text(pow) == 278


___ test_max():
    assert get_len_help_text(max) == 402


___ test_bad_input():
    max1 = object()
    with pytest.raises(ValueError):
        get_len_help_text(max1)


___ test_another_bad_input():
    with pytest.raises(ValueError):
        get_len_help_text('string')


___ test_src():
    src = inspect.getsource(get_len_help_text)
    assert 'help' in src
    assert 'redirect_stdout' in src