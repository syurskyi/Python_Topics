# # Return a new list that is the result of
# # adding element to the head (i.e. front) of input_list
# _ attach_head element input_list
#     r_ |element| + input_list
#
# print(a00_h00(1,                                                  # Will return [1, 46, -31, "hello"]
#               a00_h00(46,                                     # Will return [46, -31, "hello"]
#                       a00_h00(-31,                        # Will return [-31, "hello"]
#                               a00_h00("hello", []))))) # Will return
#
