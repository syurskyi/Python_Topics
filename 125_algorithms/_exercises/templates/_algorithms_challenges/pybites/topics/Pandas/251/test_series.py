_______ s__

_______ p.... __ pd

_______ r.. __ se


___ test_basic_series
    ser = se.b..
    ... isi..(ser, ?.S..)
    ... ?.n.. "Fred"
    ... ?.dtype __ "int64"
    ... a..(n __ [1, 2, 3, 4, 5] ___ n __ ?.values)
    ... l..(?.values) __ 5

___ test_floats_series
    ser = se.float_series()
    ... isi..(ser, ?.S..)
    ... ?.dtype __ "float64"
    ... l..(ser) __ 1001
    ... ?.s..() __ 500.5

___ test_alpha_index_series
    ser = se.a..
    ... isi..(ser, ?.S..)
    ... ?.dtype __ "int64"
    ... l..(ser) __ 26
    ... s..(?.values) __ 351
    ... a..(c __ s__.a.. ___ c __ ?.index)

___ test_object_values_series
    ser = se.o..
    ... isi..(ser, ?.S..)
    ... l..(ser) __ 26
    ... a..(c __ s__.a.. ___ c __ ?.values)
    ... ser[101] __ "A"
    ... ser[126] __ "Z"