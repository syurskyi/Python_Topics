# ____ ? _______ ?
#
# default_tree """
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************
# """
# smaller_tree """
#   *
#  ***
# *****
# """
#
#
# ___ test_height_xmas_tree
#     ... l..? .s.. '\n' __ 10  # default arg
#     ... l..? 5 .s.. '\n' __ 5
#     ... l..? 20 .s.. '\n' __ 20
#
#
# ___ test_num_stars_used
#     ... ? 3 .c.. '*' __ 9
#     ... ? 5 .c.. '*' __ 25
#     ... ? 20 .c.. '*' __ 400
#
#
# ___ test_outputs
#     actual_tree ? .s.. '\n' .s.. '\n'
#     expected_tree d__.s.. '\n' .s.. '\n'
#     ___ i, j __ z.. ? ?
#         ... ?.r.. __ ?.r..
#
#     actual_tree ? 3 .s.. '\n' .s.. '\n'
#     expected_tree s__.s.. '\n' .s.. '\n'
#     ___ i, j __ z.. ? ?
#         ... ?.r.. __ ?.r..