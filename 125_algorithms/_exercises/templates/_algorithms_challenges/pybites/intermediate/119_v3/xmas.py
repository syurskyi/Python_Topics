# ___ generate_xmas_tree rows=10
#     """Generate a xmas tree of stars (*) for given rows (default 10).
#        Each row has row_number*2-1 stars, simple example: for rows=3 the
#        output would be like this (ignore docstring's indentation):
#          *
#         ***
#        *****"""
#
#     result    # list
#     stars 1
#
#     final_row_stars =  2 * ? - 1
#
#     left_gap ?//2
#
#
#     ___ row __ r.. 1 ? + 1
#
#         stars 2 * ? - 1
#         l.. += 1
#         line _* '*'*?:> ?\n
#         __ row __ ?
#             line ?.r..
#         ?.a.. ?
#
#
#     r.. ''.j.. ?
#
#
# __ _______ __ _______
#
#     print ?
