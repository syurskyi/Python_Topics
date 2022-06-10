# _______ __
#
# DOWN, UP, LEFT, RIGHT '⇓', '⇑', '⇐', '⇒'
# START_VALUE 1
# STOP ' '
#
# ___ _seek_next grid l.., position t..
#     row, col p..
#     next_val ? ? ? + 1
#     __ r.. < l.. g.. - 1 a.. g.. r.. + 1 c.. __ ?
#         r..  r.. + 1 c.. D..
#     __ r.. > 0 a.. g.. r.. - 1 c.. __ n..
#         r.. r.. - 1 c.. U.
#     __ c.. < l.. g.. r.. -1 a.. g.. r.. c.. + 1 __ n..
#         r.. r.. c.. + 1 R..
#     __ c.. > 0 a.. g.. r.. c.. - 1 __ n..
#         r.. r.. c.. - 1 L..
#     r.. r.. c.. S..
#
#
# ___ print_sequence_route grid s.. start_coordinates_ N..
#     """Receive grid string, convert to 2D matrix of ints, find the
#        START_VALUE coordinates and move through the numbers in order printing
#        them.  Each time you turn append the grid with its corresponding symbol
#        (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
#     grid_array i.. v ___ ? __ __.f.. _ (\d+)  line
#                   ___ ? __ g...s..k.._F..
#                   __ l.. ?.r.. '|', '' .s.. > 0
#
#     start_coordinates r.. c..
#                          ___ r.. __ r.. l.. ?
#                          ___ c.. __ r.. l.. ? r..
#                          __ ? r.. c.. __ S.. 0
#
#     current_direction R..
#     current_vals s.. S..
#
#     this_val S.. + 1
#     next_coordinates s..
#     w.... c.. !_ S..
#         n.. n.. _? g.. n..
#         __ c.. __ n..
#             c__.a.. s.. t..
#         ____
#             print _* " ".j.. c.. n..
#             c.. s.. t..
#             c.. n..
#         t.. +_ 1
#
#     print('done')
