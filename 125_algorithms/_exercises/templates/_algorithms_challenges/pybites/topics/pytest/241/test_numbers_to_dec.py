_______ p__

____ numbers_to_dec _______ list_to_decimal

___ test_correct_result
    ... list_to_decimal([4]) __ 4
    ... list_to_decimal([2,3]) __ 23
    ... list_to_decimal([2,3,4]) __ 234
    ... list_to_decimal([1,2,3,4]) __ 1234
    ... list_to_decimal([0,1,2,3,4]) __ 1234

___ test_boolean
    w__ p__.r.. T..
        list_to_decimal([T..])

___ test_float
    w__ p__.r.. T..
        list_to_decimal([3.6])

___ test_string
    w__ p__.r.. T..
        list_to_decimal( '4' )


___ test_negative_int
    w__ p__.r..(ValueError
        list_to_decimal([-1])

