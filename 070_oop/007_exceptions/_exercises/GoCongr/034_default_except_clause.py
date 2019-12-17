# # default_except_clause
# t__
#     x _ 3 / 0
# e____
#     p___
#
# print('Program flow goes further')
#
# # unhandled_exception
# t__
#     r____ V...
# e____ Z.....
#     print('Division by zero')
#
# # unhandled_exception_in_inner_try
# t__
#     t__
#         r____ V...('incorrect value')
#     e____ Z.....
#         print('division by zero')
# e____ E... a_ e
#     print ?
#
# # exception_in_destructor
# class MyClass o....
#     ___ -d  _____
#         r____ Z.....
#
#
# print('Creating object')
# obj _ ?
#
# print('Deleting object')
# del obj
#
# print('Done')
#
# # raise_in_except
# t__
#     t__
#         r____ V...('value is incorrect')
#     e____ V... a_ error
#         print('Exception:', ?)
#         r____
# e____ V...
#     print('ValueError detected')
#
# # raise_another_exception_in_except
# a _ 5
# b _ 0
#
# t__
#     c _ a / b
# e____ Z.....
#     r____ V...
#
# # raise_from
# a _ 5
# b _ 0
#
# t__
#     c _ a / b
# e____ Z..... a_ error
#     r____ V...('variable b is incorrect') fr.. ?
#
# # raise_from_None
# a _ 5
# b _ 0
#
# t__
#     c _ a / b
# e____ Z..... a_ error
#     r____ V...('variable b is incorrect') fr.. N..
#
# # else
# ___ divide_numbers
#     w____ T..
#         t__
#             first_number _ float(input('First number: '))
#             second_number _ float(input('Second number: '))
#             result _ first_number / second_number
#         e____ V... Z..... a_ error
#             print('Error:', ?)
#             print('Please t__ again')
#             print()
#         e___
#             print('Result:' ?
#             b____
#
#
# __ ______ __ ______
#     ?
#
# # finally
# ___ function_that_may_fail
#     response _ N..
#     w___ ? !_ 'y' and ? !_ 'n'
#         ? _ inp.. ('r____ an exception? (y/n) ')
#     i_ ? __ 'y'
#         r____ E..
#
#
# t__
#     ?
# e____
#     print('Exception handler')
# f_____
#     print('Finally block')
#
# # t__-finally
# t__
#     2 / 0
# f____
#     print('Finally block is always executed')
