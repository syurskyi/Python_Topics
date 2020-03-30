# '''
# n=3, 3 pegs:
# start -> dest
# start -> i
# dest -> i
# start -> dest
# i -> start
# i -> dest
# start -> dest
#
# n=3, 4 pegs:
# start, i1
# start -> i2
# start -> dest
# i2 -> dest
# i1, dest
# '''
#
# ___ hanoi3 n peg_start peg_intermed peg_dest
#     __ n __ 1
#         print('@ -> @'.f.. _s.., _d..
#         r_
#
#     ?(? - 1, _s.., _d.., _i..
#     print('@-> @'.f..(_s.., _d..
#     ?(? - 1, _i.., _s.., _d..
#
# ___ hanoi4(n, peg_start, peg_intermed1, peg_intermed2, peg_dest
#     __ n __ 0
#         r_
#     __ n __ 1
#         print('@, @'.f.. _s.. _d..
#         r_
#
#     ?(n - 2, _s.., _i..2, _d.., _i..1
#     print('@-> @'.f.. _s.., _i..2
#     print('@-> @'.f.. _s.., _d..
#     print('@-> @'.f.. _i..2, _d..
#     ?(? - 2, _i..1, _i..2, _s.., _d..
#
# print('n=3, 3 pegs:')
# hanoi3(3, 'start', 'i', 'dest')
# print('\nn=3, 4 pegs:')
# hanoi4(3, 'start', 'i1', 'i2', 'dest')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
