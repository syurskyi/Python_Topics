# ___ count_islands grid
#     """
#     Input: 2D matrix, each item is [x, y] -> row, col.
#     Output: number of islands, or 0 if found none.
#     Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
#         connected vertically or horizontally  by '1's.
#     It's also preferred to check/mark the visited islands:
#     - eg. using the helper function - mark_islands().
#     """
#     # islands = 0         # var. for the counts
#     # .....some operations.....
#     # mark_islands(r, c, grid)
#     # return islands
#
#
#
#     islands 0
#     ___ row __ r.. l.. ?
#         ___ col __ r.. l.. ? 0
#             __ ? ? ? __ 1
#                 ? ? ? ?
#                 ? +_ 1
#
#
#
#     r.. ?
#
#
#
# ___ mark_islands i j grid
#     """
#     Input: the row, column and grid
#     Output: None. Just mark the visited islands as in-place operation.
#     """
#     # grid[i][j] = '#'      # one way to mark visited ones - suggestion.
#
#
#     ? ? ? '#'
#
#
#     ___ n_row,n_col __ ? + 1 ?),(? -1 ?),(? ? + 1),(? ?-1
#         __ 0 <_ ? < l.. g.. a.. 0 <_ ? < l..(g.. 0 a.. g.. ? ? __ 1
#             ? ? ? ?
