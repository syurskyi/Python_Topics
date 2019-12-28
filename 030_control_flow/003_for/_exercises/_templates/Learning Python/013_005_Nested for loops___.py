# __author__ = 'sergejyurskyj'
#
#
#
# items = ["aaa", 111, (4, 5), 2.01]   # A set of objects
# tests = [(4, 5), 3.14]               # Keys to search for
#
# print('#' * 52 + ' For all keys')
# print('#' * 52 + ' For all items')
# print('#' * 52 + ' Check for match')
# ___ key __ t..                    # For all keys
#     ___ i.. __ items               # For all items
#         __ i.. __ k..              # Check for match
#             print k.. "was found"
#             b..
#     _____
#         print k.. "not found!"
#
# print('#' * 52 + ' For all keys')
# print('#' * 52 + ' Let Python check for a match')
# ___ key __ tests                    # For all keys
#     __ k.. __ items                 # Let Python check for a match
#         print k.. "was found")
#     ____
#         print k.. "not found!")
#
#
# print('#' * 52 + ' Start empty')
# print('#' * 52 + ' Scan first sequence')
# print('#' * 52 + ' Common item?')
# print('#' * 52 + ' Add to result end')
# seq1 = "spam"
# seq2 = "scam"
# res _                              # Start empty
# ___ x __ _1                       # Scan first sequence
#     __ ? __ _2                    # Common item?
#         ?.ap.. ?                # Add to result end
# print ?
#
#
# print('#' * 52 + ' Let Python collect results')
# print x ___ ? __ _1 i_ ? __ _2 # Let Python collect results
