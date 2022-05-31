# ____ i.. _______ i..
#
# _______ p__
#
# ____ ? _______ ? ?
#
#
# ?p__.f.. s.._"module"
# ___ slice1
#     it ?
#     r.. l.. i.. ? 96
#
#
# ?p__.f.. s.._"module"
# ___ slice2
#     it ?
#     r.. l.. i.. ? 100, 217
#
#
# ___ test_iterator_islice slice1 slice2
#     ... l.. ? __ 96
#     ... l.. ? __ 117
#
#     ... ? 0 __ ? c.._'red' c.._'Stop' t.._2
#     ... ? 0 __ ? c.._'green' c.._'Go' t.._2
#
#     ... ? -1 __ ? c.._'amber' c.._'Caution' t.._0.5
#     ... ? -1 __ ? c.._'red' c.._'Stop' t.._2
#
#
# ___ test_equal_values_in_islice slice1
#     ___ color __ 'red green amber'.s..
#         ... s.. 1 ___ state __ ? __ ?.c.. __ ? __ 32
#
#
# ___ test_return_types slice2
#     ... a..(t.. state __ S.. ___ ? __ ?
#
#
# ?p__.m__.p. "color, expected",
#     ('red', 64),
#     ('green', 64),
#     ('amber', 16),
#
# ___ test_timings slice1 color e..
#     timeout_for_color s.. state.t.. ___ ? __ ?
#                             __ ?.c.. __ ?
#     ... ? __ e..