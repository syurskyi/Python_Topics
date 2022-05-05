# _______ s__
#
# _______ p__
# _______ p.... __ pd
#
# _______ series __ se
#
# file_name "https://bites-data.s3.us-east-2.amazonaws.com/iris.csv"
# df __.r.. ?
#
#
# ?p__.f..
# ___ sepal_length_series
#     """Returns the Sepal Length Series from the Iris DataFrame"""
#     r.. __.s__.s__ .r.. d.._T..
#
#
# ?p__.f..
# ___ int_series_vsmall
#     """Returns a pandas Series containing ints"""
#     r.. ?.S.. r.. 1, 6
#
#
# ?p__.f..
# ___ int_series_small
#     """Returns a pandas Series containing ints"""
#     r.. ?.S.. r.. 10
#
#
# ?p__.f..
# ___ int_series_vsmall_offset_index
#     """Returns a pandas Series containing ints"""
#     r.. ?.S.. r.. 0, 10, 2), i.._r.. 0, 10, 2
#
#
# ?p__.f..
# ___ letters_series
#     """Returns a pandas Series containing all lower case letters"""
#     r.. ?.S.. l.. s__.a..
#
#
# ?p__.m__.p.
#     "arg, expected",
#
#         "a.. 5), [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
#         "a.. 0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#         "a.. -15), [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6]),
#         "s.. 5), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]),
#         "s.. 0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#         "s.. -15), [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),
#         "m.. 5), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]),
#         "m.. 0), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
#         "m.. -15), [0, -15, -30, -45, -60, -75, -90, -105, -120, -135]),
#         "d.. 5), [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]),
#         "d.. -5), [-0.0, -0.2, -0.4, -0.6, -0.8, -1.0,
#                        -1.2, -1.4, -1.6, -1.8
#
#
# ___ test_series_simple_math int_series_small arg e..
#     ... a..
#         e.. idx __ val
#         ___ ? ? __ e..
#             s_.s.. ? ? 0 ? 1
#
#
#
#
# ?p__.m__.p.
#     "arg, expected",
#
#         "a.. [1.0, "nan", 5.0, "nan", 9.0, "nan", "nan"]),
#         "s.. [1.0, "nan", 1.0, "nan", 1.0, "nan", "nan"]),
#         "m.. [0.0, "nan", 6.0, "nan", 20.0, "nan", "nan"]),
#         "d.. ["inf", "nan", 1.5, "nan", 1.25, "nan", "nan"]),
#
#
# ___ test_complex_series_maths
#     int_series_vsmall i.. a.. e..
#
#     result s_.c..
#         i.. i.. arg
#
#     result ",".j.. s..(n) ___ ? __ ?
#     e.. ",".j.. s..(n) ___ ? __ e..
#     ... ? __ e..
#
#
# ?p__.m__.p.
#     "arg, expected",
#
#
#             ["a", "e", "i", "o", "u"],
#
#                 T..
#                 F..
#                 F..
#                 F..
#                 T..
#                 F..
#                 F..
#                 F..
#                 T..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 T..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 T..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#
#
#
#             ["j", "k", "q", "x", "z"],
#
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 T..
#                 T..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 T..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 F..
#                 T..
#                 F..
#                 T..
#
#
#
#
# ___ test_create_series_mask letters_series arg e..
#     result s_. ? ? ?
#     ... a.. ? idx __ exp ___ ? ? __ e.. e..
#     ... a.. l __ ? ___ ? __ l.. ?
#
#
# ___ test_custom_series_function sepal_length_series
#     result s_. ? ? 0.1
#     ... l.. ? __ 51
#     ... r.. ?.m.. 4) __ 5.6725
#     ... m.. ?.i.. __ 149 a.. m.. ?.v.. __ 7.9
#     ... m.. ?.i.. __ 0 a.. m.. ?.v.. __ 4.3
#     ... ?[82] __ 5.9
#     ... ? i.. 10 __ 5.0
#     ... ? i.. 11 __ 5.1
#     ... ? i.. 20 __ 5.7
#     ... ? i.. 37 __ 5.9
#     ... ? i.. 38 __ 6.4
