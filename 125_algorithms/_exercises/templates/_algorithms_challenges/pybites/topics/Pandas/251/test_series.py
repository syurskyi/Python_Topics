_______ s__

_______ pandas __ pd

_______ series __ se


___ test_basic_series
    ser = se.basic_series()
    ... isi..(ser, pd.Series)
    ... ser.name __ "Fred"
    ... ser.dtype __ "int64"
    ... a..(n __ [1, 2, 3, 4, 5] ___ n __ ser.values)
    ... l..(ser.values) __ 5

___ test_floats_series
    ser = se.float_series()
    ... isi..(ser, pd.Series)
    ... ser.dtype __ "float64"
    ... l..(ser) __ 1001
    ... ser.s..() __ 500.5

___ test_alpha_index_series
    ser = se.alpha_index_series()
    ... isi..(ser, pd.Series)
    ... ser.dtype __ "int64"
    ... l..(ser) __ 26
    ... s..(ser.values) __ 351
    ... a..(c __ s__.ascii_lowercase ___ c __ ser.index)

___ test_object_values_series
    ser = se.object_values_series()
    ... isi..(ser, pd.Series)
    ... l..(ser) __ 26
    ... a..(c __ s__.a.. ___ c __ ser.values)
    ... ser[101] __ "A"
    ... ser[126] __ "Z"