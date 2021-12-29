import pytest

from numbers_to_dec import list_to_decimal




___ test_single_element():

    assert list_to_decimal([4]) == 4


___ test_padding_zero():

    assert list_to_decimal([0,4,2,3]) == 423


___ test_large_list():
    assert list_to_decimal([1,2,3,4,5,6]) == 1223456

___ test_out_of_range():


    with pytest.raises(ValueError):
        list_to_decimal([12,5,4])


___ test_invalid_type_string():
    with pytest.raises(ValueError):
        list_to_decimal([12,'5',4])



___ test_invalid_type_boolean():
    with pytest.raises(ValueError):
        list_to_decimal([12,True,4])


___ test_negative():
    with pytest.raises(ValueError):
        list_to_decimal([-3,12])



___ test_float():
    with pytest.raises(ValueError):
        list_to_decimal([4.5,4,1])
