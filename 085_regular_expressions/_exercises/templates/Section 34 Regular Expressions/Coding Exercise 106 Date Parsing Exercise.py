# Date Parsing Solution
#
# My regex for dates looks like this:
#
# ^(\d\d)[,/.](\d\d)[,/.](\d{4})$
#
# Two digits followed by either a comma, slash, or period.  Then two more digits followed by either a comma, slash,
# or period.  And then 4 more digits.  I used parens to form capture groups for the 3 sections.
#
# Then, I simply referenced those capture groups using match.group(1) or match.group(2), etc.

# ________ __
# ___ parse_date input
#     pattern = __.c...  _ 1?|?2?2 |,/.| |?2?2 |,/.| 2? 3? 4?  # 1. Starts with
#                                                            # 2. Returns a match where the string contains digits (numbers from 0-9)
#                                                            # 3. Exactly the specified number of occurrences - 4
#                                                            # 4. Ends with
#
#     match = ?.s.. ?
#     __ ?
#         r_ {
#             "d": m...g.. 1
#             "m": m...g.. 2
#             "y": m...g.. 3
#         }
#     r_ N..