_______ i___
_______ s__

_______ p__
_______ n.... __ np
_______ p.... __ pd

_______ series __ se


?p__.f..
___ float_series
    """Returns a pandas Series containing floats"""
    r.. ?.S..([f__(n) / 1000 ___ n __ r..(0, 1001)])


?p__.f..
___ alpha_series
    """Returns a pandas Series containing floats"""
    dictionary d..(z..(s__.a.., r..(1, 27)))
    r.. ?.S..(dictionary)


?p__.m__.p.("arg, expected", [
    (0, 0.000), (500, 0.500), (1000, 1.000)
])
___ test_return_at_index(float_series, arg, e..
    ... se.return_at_index(float_series, arg) __ e..

___ test_return_at_index_raise_exception(float_series
    w__ p__.r..(K..
        float_series[1111]

___ test_get_slice(float_series
    slce se.get_slice(float_series, 20, 25)
    ... isi..(slce, pd.core.series.S..)
    ... l..(slce) __ 5
    ... slce[24] __ 0.024

___ test_get_slice_inclusive(float_series
    slce ?.g.. ? 20, 25)
    ... isi..(slce, pd.core.series.S..)
    ... l..(slce) __ 6
    ... slce[25] __ 0.025

?p__.m__.p.("arg, expected", [
    (0, 0.000), (5, 0.005), (9, 0.009)
])
___ test_return_head(float_series, arg, e..
    ... se.return_head(float_series, 10)[arg] __ e..
    ... ".head" __ i___.g.. se.return_head)

?p__.m__.p.("arg, expected", [
    (991, 0.991), (995, 0.995), (1000, 1.000)
])
___ test_return_tail(float_series, arg, e..
    ... se.return_tail(float_series, 10)[arg] __ e..
    ... ".tail" __ i___.g.. se.return_tail)

___ test_get_index(alpha_series
    idx se.get_index(alpha_series)
    ... isi..(idx, pd.core.indexes.base.Index)
    ... l..(idx) __ 26
    ... a..(c __ s__.a.. ___ c __ idx.values)
    ... ".index" __ i___.g.. se.get_index)

___ test_get_values(alpha_series
    vals se.get_values(alpha_series)
    ... isi.. ? np.ndarray)
    ... l..(vals) __ 26
    ... a..(c __ r..(1, 27) ___ c __ vals)

___ test_all_even_indexes_returned(float_series
    ser se.get_every_second_indexes(float_series, T..)
    ... a..(n % 2 __ 0 ___ n __ ?.index)
    ... r..(s..(ser), 1) __ 250.5

___ test_all_odd_indexes_returned(float_series
    ser se.get_every_second_indexes(float_series, F..)
    ... a..(n % 2 __ 1 ___ n __ ?.index)
    ... r..(s..(ser), 1) __ 250.0