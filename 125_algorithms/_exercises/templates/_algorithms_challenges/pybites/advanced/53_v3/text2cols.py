# ____ i.. _______ z__
#
# COL_WIDTH 20
#
#
# ___ _divide_line line s.., col_width i.. ?
#     words ?.s..
#     result    # list
#     line ? 0
#     ___ word __ ? 1|
#         line2 ? + ' ' + ?
#         __ l.. ? > c..
#             ?.a.. l..
#             l.. w..
#         ____
#             l.. l..
#     ?.a.. ?
#     r.. ?
#
#
# ___ text_to_columns text
#     """Split text (input arg) to columns, the amount of double
#        newlines (\n\n) in text determines the amount of columns.
#        Return a string with the column output like:
#        line1\nline2\nline3\n ... etc ...
#        See also the tests for more info."""
#     lines ? col ___ ? __ ?.s.. '\n\n'
#     rv =  ' '.j.. combination ___ ? __ z__ *? fillvalue_' '
#     r.. '\n'.j.. >
