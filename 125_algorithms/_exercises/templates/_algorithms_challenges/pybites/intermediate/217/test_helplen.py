import inspect

import pytest

from helplen import get_len_help_text


___ test_pow():
    # py 3.7 / 3.8 difference
    assert get_len_help_text(pow) in (278, 284)

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