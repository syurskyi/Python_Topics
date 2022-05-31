# _______ textwrap
# _______ i..
#
# COL_WIDTH 20
#
#
# ___ text_to_columns text
#     """Split text (input arg) to columns, the amount of double
#        newlines (\n\n) in text determines the amount of columns.
#        Return a string with the column output like:
#        line1\nline2\nline3\n ... etc ...
#        See also the tests for more info."""
#
#
#     paragraphs ?.s.. '\n\n'
#     number_of_columns l.. ?
#
#     l    # list
#     ___ paragraph __ p..
#         p.. ?.s..
#         r t__.w.. ? w.._C.. break_long_words_T..
#         l.a.. ?
#
#
#     result    # list
#     ___ p __ i...z__ *l,fillvalue=''
#
#         line    # list
#         ___ value __ p
#             line.a.. _* ?:<25
#
#             #result.append(f"{value:<25}",end='')
#             #print(f"{value:<25}",end='')
#         #print()
#
#         result.a.. ''.j.. ?
#
#
#     r.. '\n'.j.. ?
#
# __ _______ __ _______
#
#
#     text """My house is small but cosy.
#
#     It has a white kitchen and an empty fridge."""
#     text """My house is small but cosy.
#
#     It has a white kitchen and an empty fridge.
#
#     I have a very comfortable couch, people love to sit on it."""
#
#
#     ? ?
#
