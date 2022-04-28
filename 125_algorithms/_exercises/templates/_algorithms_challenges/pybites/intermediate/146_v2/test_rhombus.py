# ____ ? _______ ?
#
#
# ___ test_rhombus_width3
#     # recommended: actual before expected
#     # https://twitter.com/brianokken/status/1063337328553295876
#     a.. l.. ? 3
#     e.. =  ' * ', '***', ' * '
#     ... a.. __ e..
#
#
# ___ test_rhombus_width5
#     a.. l.. ? 5
#     e.. =  '  *  ', ' *** ', '*****',
#                 ' *** ', '  *  '
#     ... a.. __ e..
#
#
# ___ test_rhombus_width11
#     """print('\n'.join(expected)) would give (ignore indents):
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#      *********
#       *******
#        *****
#         ***
#          *
#     """
#     a.. l.. ? 11
#     e.. =  '     *     ', '    ***    ', '   *****   ',
#                 '  *******  ', ' ********* ', '***********', ' ********* ',
#                 '  *******  ', '   *****   ', '    ***    ', '     *     '
#     ... a.. __ e..