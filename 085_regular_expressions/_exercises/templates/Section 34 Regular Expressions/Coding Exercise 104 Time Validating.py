# # Time Validating Solution
# #
# # The regular expression I used is:
# #
# #     ^\d\d?:\d\d$
# #
# # The time must start with a digit, and there can be a second optional digit before the colon.
# # Then there's the colon and two mandatory digits.
# # I used ^ and $ to make sure the time was the only thing in the input string.
# #
# # Here's the full solution:
#
# _____ __
#
#
# ___ is_valid_time input
#     pattern = __.c..  _ 1? 2? 2? 3? 2? 2? 4?  # 1. Starts with
#                                            # 2. Returns a match where the string contains digits (numbers from 0-9)
#                                            # 3. Groups regular expressions without remembering matched text.
#                                            # 4. end with
#     match = ?.s.. ?
#     __ ?
#         r_ T..
#     r_ F..
