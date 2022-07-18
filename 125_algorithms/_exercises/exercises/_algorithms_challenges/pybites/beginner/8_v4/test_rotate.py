# ____ r.. _______ r..
#
#
# ___ test_small_rotate
#     ... ? 'hello', 2 __ 'llohe'
#     ... ? 'hello', -2 __ 'lohel'
#
#
# ___ test_bigger_rotation_of_positive_n
#     string  'bob and julian love pybites!'
#     expected  'love pybites!bob and julian '
#     ... ?(?, 15) __ ?
#
#
# ___ test_bigger_rotation_of_negative_n
#     string = 'pybites loves julian and bob!'
#     expected = 'julian and bob!pybites loves '
#     ... ? ? -15 __ ?
#
#
# ___ test_rotation_of_n_same_as_len_str
#     string = expected = 'julian and bob!'
#     ... ? ?, l.. ? __ ?
#
#
# ___ test_rotation_of_n_bigger_than_string
#     string = 'julian and bob!'
#     expected_solution1 = 'julian and bob!'
#     expected_solution2 = ' bob!julian and'  # ;)
#     ... ? ?, 100 __ ? ?
#
#     # should be the same as doing a ? with modulo
#     # which is 100 % 15 (len string) => n=10
#     mod  100 % l..(?)  # 10
#     ... ? ? ? __  ? ?