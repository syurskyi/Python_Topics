# ______ __
#
#
# c_ Mind
#
#     ___  -
#         p_
#
#     ___ think  query
#         __ 'sum' __ ?  # Check if string 'sum' is in query
#             numbers _ __.f_a_(r'\b\d+\b' ?  # Extract the numbers. E.g. ['1', '2']
#             numbers _ fl.. item ___ ? __ ?  # Convert the numbers into floats [1.0, 2.0]
#             r_ su. ?  # Return the sum of the numbers
#
#
# c_ Robot
#
#     ___  -
#         mind _ ?  # When Robot is initialized with Robot(), that will also initialize Mind
#
#     ___ print_out query
#         mind _ ?  # When Robot is initialized with Robot(), that will also initialize Mind
#         print ?.t.. ?  # Prints out the output returned by mind.think(query)
#
#     ___ write_down query
#         mind _ ?  # When Robot is initialized with Robot(), that will also initialize Mind
#
#         w__ o.. "new.txt" _ __ file
#             ?.w.. st. ?.t.. ?
