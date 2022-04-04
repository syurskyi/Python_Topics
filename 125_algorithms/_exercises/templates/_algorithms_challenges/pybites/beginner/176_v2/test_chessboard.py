# ____ textwrap _______ dedent  # thanks Brian :)
#
# _______ p__
#
# ____ ? _______ ?
#
# sizes  [2, 4, 8, 16, 32]
# outputs  [
#     """
#      #
#     #
#     """,
#     """
#      # #
#     # #
#      # #
#     # #
#     """,
#     """
#      # # # #
#     # # # #
#      # # # #
#     # # # #
#      # # # #
#     # # # #
#      # # # #
#     # # # #
#     """,
#     """
#      # # # # # # # #
#     # # # # # # # #
#      # # # # # # # #
#     # # # # # # # #
#      # # # # # # # #
#     # # # # # # # #
#      # # # # # # # #
#     # # # # # # # #
#      # # # # # # # #
#     # # # # # # # #
#      # # # # # # # #
#     # # # # # # # #
#      # # # # # # # #
#     # # # # # # # #
#      # # # # # # # #
#     # # # # # # # #
#     """,
#     """
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#      # # # # # # # # # # # # # # # #
#     # # # # # # # # # # # # # # # #
#     """,
#
# expected_outputs  d..z.. ? ?
#
#
# ___ _non_empty_lines output
#     """Helper to turn a string into a list of not
#        empty lines and returns it.
#     """
#     r.. line ___ ? __ ?.s..  __ ?.s..
#
#
# ?p__.m__.p. "size" ?
# ___ test_create_chessboard size capfd
#     ? ?
#     actual  ?.r .. 0]
#     expected  ? ? ?
#     ... ? ? __ ? ?