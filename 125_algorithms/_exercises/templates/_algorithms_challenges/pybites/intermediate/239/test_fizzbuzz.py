# _______ p__
# ____ ? _______ ?
#
# # prepare test data
# div_3 l.. r.. 3, 3*100 + 1, 3
# del ? 4||5
# div_5 l.. f.. l.... x ?%3 !_ 0, r..(5, 5*100 + 1, 5
# div_15 l..(r..(15, 15*30 + 1, 15
# others x ___ ? __ r..(1,3*100 + 1) __ ? n.. __ ?_3
#           a.. ? n.. __ ?_5 a.. ? n.. __ ?_15
#
#
#
# # write one or more pytest functions below, they need to start with test_
# ?p__.m__.p. 'arg' ?_3
# ___ test_div_by_3 arg
#     ''' tests only numbers divisible by 3 and not 5 '''
#     ... ? ? __ 'Fizz'
#
#
# ?p__.m__.p. 'arg' ?_5
# ___ test_div_by_5 arg
#     ''' tests number only divisible by 5--not 3'''
#     ... ? ? __ 'Buzz'
#
#
# ?p__.m__.p. 'arg' ?_15
# ___ test_div_by_3_5 arg
#     ''' tests numbers divisible by both 3 and 5'''
#     ... ? ? __ 'Fizz Buzz'
#
#
# ?p__.m__.p. 'arg' others
# ___ test_others arg
#     ''' tests numbers not divisible by 3 or 5'''
#     ... ? ? __ ?
