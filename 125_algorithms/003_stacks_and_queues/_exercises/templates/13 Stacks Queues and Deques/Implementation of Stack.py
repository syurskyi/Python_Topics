# # Implementation of Stack
# # Stack Attributes and Methods
# #
# # Before we implement our own Stack class, let's review the properties and methods of a Stack.
# #
# # The stack abstract data type is defined by the following structure and operations. A stack is structured,
# # as described above, as an ordered collection of items where items are added to and removed from the end called
# # the top. Stacks are ordered LIFO. The stack operations are given below.
# #
# #     Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
# #     push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
# #     pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
# #     peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not
# #     modified.
# #     isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
# #     size() returns the number of items on the stack. It needs no parameters and returns an integer.
# #
# # Stack Implementation
#
# c_ Stack
#
#     ___ __init__
#         items  _   # list
#
#     ___ isEmpty
#         r_ ? __    # list
#
#     ___ push  item
#         ?.ap.. ?
#
#     ___ pop
#         r_ ?.p..
#
#     ___ peek
#         r_ ? le. ? - 1
#
#     ___ size
#         r_ le. ?
#
# # Let's try it out!
#
# s = ?
#
# print ?.iE...
# # True
#
# ?.p.. 1
# ?.p.. 'two'
# ?.pe..
# # 'two'
#
# ?.p.. T..
# ?.s..
# # 3
#
# # ?.isEmpty()
# F..
#
# ?.p..
# # True
#
# ?.p..
# # two
#
# ?.s..
# # 1
#
# ?.p..
# # 1
#
# ?.iE..
# # True
