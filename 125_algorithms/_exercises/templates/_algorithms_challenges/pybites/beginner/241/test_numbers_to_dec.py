_______ pytest

____ numbers_to_dec _______ list_to_decimal




___ test_single_element():

    ... list_to_decimal([4]) __ 4


___ test_padding_zero():

    ... list_to_decimal([0,4,2,3]) __ 423


___ test_large_list():
    ... list_to_decimal([1,2,3,4,5,6]) __ 1223456

___ test_out_of_range():


    with pytest.raises(ValueError):
        list_to_decimal([12,5,4])


___ test_invalid_type_string():
    with pytest.raises(ValueError):
        list_to_decimal([12,'5',4])



___ test_invalid_type_boolean():
    with pytest.raises(ValueError):
        list_to_decimal([12,T..,4])


___ test_negative():
    with pytest.raises(ValueError):
        list_to_decimal([-3,12])



___ test_float():
    with pytest.raises(ValueError):
        list_to_decimal([4.5,4,1])
