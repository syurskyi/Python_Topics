# _______ s__
# _______ n.... __ np
# _______ p.... __ pd
#
#
# ___ basic_series __ ?.S..
#     """Create a pandas Series containing the values 1, 2, 3, 4, 5
#     Don't worry about the indexes for now.
#     The name of the series should be 'Fred'
#     """
#     r.. ?.S.. r.. 1,6 name 'Fred'
#
#
# ___ float_series __ ?.S..
#     """Create a pandas Series containing the all the values
#     from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
#     Don't worry about the indexes or the series name.
#     """
#
#     r.. ?.S.. ?.a.. 0.000,1.001,0.001
#
#
#
# ___ alpha_index_series __ ?.S..
#     """Create a Series with values 1, 2, ... 25, 26 of type int64
#     and add an index with values a, b, ... y, z
#     so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
#     Don't worry about the series name.
#     """
#     r.. ?.S.. r.. 1,27 dtype_'int64' index_l.. s__.a..
#
#
# ___ object_values_series __ ?.S..
#     """Create a Series with values A, B, ... Y, Z of type object
#     and add an index with values 101, 102, ... 125, 126
#     so index 101='A', 102='B' ... 125='Y', 126='Z'
#     Don't worry about the series name.
#     """
#
#     r.. ?.S.. l.. s__.a.. index_r.. 101,127
