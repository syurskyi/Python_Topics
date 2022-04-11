# _______ i___
# _______ s__
#
# _______ p__
# _______ n.... __ np
# _______ p.... __ pd
#
# _______ series __ se
#
#
# ?p__.f..
# ___ float_series
#     """Returns a pandas Series containing floats"""
#     r.. ?.S.. f__(n) / 1000 ___ ? __ r.. 0 1001
#
#
# ?p__.f..
# ___ alpha_series
#     """Returns a pandas Series containing floats"""
#     dictionary  d.. z.. s__.a.. r.. 1 27
#     r.. ?.S.. ?
#
#
# ?p__.m__.p. "arg, expected", [
#     (0, 0.000), (500, 0.500), (1000, 1.000)
#
# ___ test_return_at_index float_series arg e..
#     ... ?.r..? ? __ e..
#
#
# ___ test_return_at_index_raise_exception float_series
#     w__ p__.r.. K..
#         ? 1111
#
#
# ___ test_get_slice float_series
#     slce  ?.g.. ? 20 25
#     ... isi.. ? ?.c__.s__.S..
#     ... l.. ? __ 5
#     ... ? 24 __ 0.024
#
#
# ___ test_get_slice_inclusive float_series
#     slce  ?.g.. ? 20 25
#     ... isi.. ? ?.c__.s__.S..
#     ... l.. ? __ 6
#     ... ? 25 __ 0.025
#
#
# ?p__.m__.p. "arg, expected", [
#     (0, 0.000), (5, 0.005), (9, 0.009)
#
# ___ test_return_head float_series arg e..
#     ... ?.r.. ? 10 ? __ e..
#     ... ".head" __ i___.g.. ?.r..
#
#
# ?p__.m__.p. "arg, expected", [
#     (991, 0.991), (995, 0.995), (1000, 1.000)
#
# ___ test_return_tail float_series arg e..
#     ... ?.r.. f.. 10 ? __ e..
#     ... ".tail" __ i___.g.. ?.r..
#
#
# ___ test_get_index alpha_series
#     idx  ?.g.. ?
#     ... isi.. ? ?.c__.i__.b...I..
#     ... l.. ? __ 26
#     ... a.. c __ s__.a.. ___ c __ ?.v..
#     ... ".index" __ i___.g.. ?.g..
#
#
# ___ test_get_values alpha_series
#     vals  ?.g.. ?
#     ... isi.. ? ?.n..
#     ... l.. ? __ 26
#     ... a.. c __ r.. 1 27 ___ ? __ ?
#
#
# ___ test_all_even_indexes_returned float_series
#     ser  ?.g.. ? T..
#     ... a.. n % 2 __ 0 ___ ? __ ?.i..
#     ... r.. s.. ? 1 __ 250.5
#
#
# ___ test_all_odd_indexes_returned float_series
#     ser  ?.g.. ? F..
#     ... a.. n % 2 __ 1 ___ ? __ ?.i..
#     ... r.. s.. ? 1 __ 250.0