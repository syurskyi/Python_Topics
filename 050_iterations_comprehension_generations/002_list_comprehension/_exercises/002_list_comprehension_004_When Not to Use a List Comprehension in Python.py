# # List comprehensions are useful and can help you write elegant code that’s easy to read and debug, but they’re
# # not the right choice for all circumstances. They might make your code run more slowly or use more memory.
# # If your code is less performant or harder to understand, then it’s probably better to choose an alternative.
# # Watch Out for Nested Comprehensions
# # Comprehensions can be nested to create combinations of lists, dictionaries, and sets within a collection.
# # For example, say a climate laboratory is tracking the high temperature in five different cities for the first
# # week of June. The perfect data structure for storing this data could be a Python list comprehension nested within
# # a dictionary comprehension:
#
# cities _ 'Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte'
# temps _ city |0 ___ _ __ ra.. 7| ___ ? __ ?    # _ the first is original # dict
# print ?
# # {
# #     'Austin': [0, 0, 0, 0, 0, 0, 0],
# #     'Tacoma': [0, 0, 0, 0, 0, 0, 0],
# #     'Topeka': [0, 0, 0, 0, 0, 0, 0],
# #     'Sacramento': [0, 0, 0, 0, 0, 0, 0],
# #     'Charlotte': [0, 0, 0, 0, 0, 0, 0]
# # }
#
# # You create the outer collection temps with a dictionary comprehension. The expression is a key-value pair,
# # which contains yet another comprehension. This code will quickly generate a list of data for each city in cities.
# # Nested lists are a common way to create matrices, which are often used for mathematical purposes.
# # Take a look at the code block below:
#
# matrix _ ||i ___ ? __ ra.. 5  ___ _ __ ra.. 6   # _ the first is original # dict
# print m...
# # [
# #     [0, 1, 2, 3, 4],
# #     [0, 1, 2, 3, 4],
# #     [0, 1, 2, 3, 4],
# #     [0, 1, 2, 3, 4],
# #     [0, 1, 2, 3, 4],
# #     [0, 1, 2, 3, 4]
# # ]
#
# # The outer list comprehension [... for _ in range(6)] creates six rows, while the inner list comprehension
# # [i for i in range(5)] fills each of these rows with values.
# # So far, the purpose of each nested comprehension is pretty intuitive. However, there are other situations,
# # such as flattening nested lists, where the logic arguably makes your code more confusing.
# # Take this example, which uses a nested list comprehension to flatten a matrix:
#
# matrix _
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 2],
#
# flat _ num ___ row __ ? ___ n.. __ r..
# print ?
# # [0, 0, 0, 1, 1, 1, 2, 2, 2]
#
# # The code to flatten the matrix is concise, but it may not be so intuitive to understand how it works.
# # On the other hand, if you were to use for loops to flatten the same matrix, then your code will be much
# # more straightforward:
#
# matrix _ [
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 2],
# ]
# flat _     # List
# ___ row __ m..
#     ___ num __ r..
#         f__.ap.. n..
#
# print f..
# # [0, 0, 0, 1, 1, 1, 2, 2, 2]
#
# # Now you can see that the code traverses one row of the matrix at a time, pulling out all the elements in that
# # row before moving on to the next one.
# # While the single-line nested list comprehension might seem more Pythonic, what’s most important is to write
# # code that your team can easily understand and modify. When you choose your approach, you’ll have to make
# # a judgment call based on whether you think the comprehension helps or hurts readability.
