# # Parsing Bytes Solution
# #
# # My regex looks like this: '\b[10]{8}\b'   It consists of eight 1s or 0s, surrounded by word boundaries on either side.
# # Remember a word boundary is either a space or the start/end of a line.
# # I then used findall  rather than search, to return a list of all matches.  Here's the final solution:
# #
#
# ______ __
# # ___ parse_bytes input
# #     binary_regex _ __.c.. _ 1?  10 2? 1?    # 1. Returns a match where the specified characters are at the beginning or at the end of a word
# #                                             # 2. любую цифру ровно 8 раз
# #     results = ?.f_a_ ?
# #     r_ ?