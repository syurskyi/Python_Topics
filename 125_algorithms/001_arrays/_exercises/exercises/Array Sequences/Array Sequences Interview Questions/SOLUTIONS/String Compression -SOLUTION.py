# # String Compression
# # Problem
# #
# # Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can
# # falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to r_ 'A2B1' even
# # though this technically takes more space.
# # The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
# # Solution
# # Since Python strings are immutable, we'll need to work off of a list of characters, and at the end convert that list
# # back into a string with a join statement.
# # The solution below should yield us with a Time and Space complexity of O(n). Let's take a look with careful attention
# # to the explanatory comments:
#
# ___ compress s
#     """
#     This solution compresses without checking. Known as the RunLength Compression algorithm.
#     """
#
#     # Begin Run as empty string
#     r = ""
#     l = le. ?
#
#     # Check for length 0
#     __ l __ 0
#         r_ ""
#
#     # Check for length 1
#     if l == 1:
#         r_ ? + "1"
#
#     # Intialize Values
#     last = ? 0
#     cnt = 1
#     i = 1
#
#     w____ ? < l
#
#         # Check to see if it is the same letter
#         __ ? ? __ ? ? - 1
#             # Add a count if same as previous
#             c.. +_ 1
#         _____
#             # Otherwise store the previous data
#             r = r + ? ? - 1 + st. c..
#             c.. _ 1
#
#         # Add to index count to terminate while loop
#         ? +_ 1
#
#     # Put everything back into run
#     r = r + ? ? - 1 + st. c..
#
#     r_ r
#
# # compress('AAAAABBBBCCCC')
# # 'A5B4C4'
#
# # Test Your Solution
# # """
# # RUN THIS CELL TO TEST YOUR SOLUTION
# # """
# # ____ n__.t.. ____ a_e..
# #
# # c_ TestCompress o..
# #
# #     ___ test  sol
# #         a_e.. ? ''), '')
# #         a_e.. ? 'AABBCC'), 'A2B2C2')
# #         a_e.. ? 'AAABCCDDDDD'), 'A3B1C2D5')
# #         print('ALL TEST CASES PASSED')
# #
# # # Run Tests
# # t _ ?
# # ?.t.. ?