# # Generators Are Single-Iteration Objects
# # My iterator is myself: G has __next__
# # Iterate manually
# # Second iterator at same position!
# # Collect the rest of I1's items
# # Other iterators exhausted too StopIteration
# # Ditto for new iterators
# # New generator to start over
#
# G _  c * 4 ___ c i_ 'SPAM'
# print it.. G  is G   # My iterator is myself: G has __next__
# # True
#
# G _  c * 4 ___ c i_ 'SPAM'   # Make a new generator
# I1 _ it.. G   # Iterate manually
# print ne.. I1
# print ne.. I1
#
# I2 _ it.. G   # Second iterator at same position!
# print ne.. I2
#
# print li.. I1   # Collect the rest of I1's items
# # print ne.. I2                             # Other iterators exhausted too StopIteration
#
# I3 _ it.. G   # Ditto ___ new iterators
# # print ne.. I3                           # StopIteration
#
# I3 _ it.. c * 4 ___ c i_ 'SPAM'   # New generator to start over
# print ne.. I3
#
# # Generators Are Single-Iteration Objects
# # Generator functions work the same way
# # like generator expression
#
# def timesfour S
#     ___ c i_ S:
#         y____ c * 4
#
#
# G _ timesfour 'spam'   # Generator functions work the same way
#
# print it.. G  is G
#
# I1, I2 _ it.. G , it.. G
#
# print ne.. I1
# print ne.. I1
# print ne.. I2   # I2 at same position as I1
#
# # Generators Are Single-Iteration Objects
# # Lists support multiple iterators
# #  Changes reflected in iterators
#
# L _ [1, 2, 3, 4]
#
# I1, I2 _ it.. L , it.. L
#
# print ne.. I1
# print ne.. I1   # Lists support multiple iterators
# print ne.. I2
#
# del L 2;  # Changes reflected in iterators
#
# # print ne.. I1                      # StopIteration
