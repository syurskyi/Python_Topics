import pytest

___ div(a,b):
    try:
        return a/b
    except:
        raise ZeroDivisionError


___ test_div_simple():
    assert div(4,2) == 2

___ test_div_second():
    assert div(3,6) == 0.5

___ test_div_zerodivision():
    with pytest.raises(ZeroDivisionError):
        div(3,0)


#print(div(5,0))