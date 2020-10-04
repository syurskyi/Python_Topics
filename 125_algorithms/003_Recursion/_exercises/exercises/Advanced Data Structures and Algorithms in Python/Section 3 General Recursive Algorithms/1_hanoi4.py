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
#         print '@ -> @'.f.. p_s.. p_d
#         r_
#
#     _3 ? - 1 p_s.. p_d.. p_i..
#     print('@ -> @'.f.. p_s.. p_d..
#     hanoi3(n - 1, p_i.., p_s.. p_d..
#
# ___ hanoi4 n, p_s.. peg_intermed1 peg_intermed2 p_d..
#     __ n __ 0
#         r_
#     __ n __ 1
#         print('@, @'.f.. p_s.. p_d..
#         r_
#
#     _4 ? - 2 p_s.., p_i2 p_d.. p_i1
#     print('@ -> @'.f.. p_s.. p_i2
#     print('@ -> @'.f.. p_s.. p_d..
#     print('@ -> @'.f..(p_i2 p_d..
#     hanoi4 ?- 2 peg_i1 p_i2 p_s.., p_d..
#
# print 'n=3, 3 pegs:'
# hanoi3(3, 'start', 'i', 'dest')
# print('\nn=3, 4 pegs:')
# hanoi4(3, 'start', 'i1', 'i2', 'dest')

