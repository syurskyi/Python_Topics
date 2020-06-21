# # default_except_clause
# ___
#     x _ 3 / 0
# _____
#     p___
#
# print('Program flow goes further')
#
# # unhandled_exception
# ___
#     r____ V...
# _____ Z.....
#     print('Division by zero')
#
# # unhandled_exception_in_inner_try
# ___
#     ___
#         r____ V...('incorrect value')
#     _____ Z.....
#         print('division by zero')
# _____ E... __ e
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
# ___
#     ___
#         r____ V...('value is incorrect')
#     _____ V... a_ error
#         print('Exception:', ?)
#         r____
# _____ V...
#     print('ValueError detected')
#
# # raise_another_exception_in_except
# a _ 5
# b _ 0
#
# ___
#     c _ a / b
# _____ Z.....
#     r____ V...
#
# # raise_from
# a _ 5
# b _ 0
#
# ___
#     c _ a / b
# _____ Z..... a_ error
#     r____ V...('variable b is incorrect') fr.. ?
#
# # raise_from_None
# a _ 5
# b _ 0
#
# ___
#     c _ a / b
# _____ Z..... a_ error
#     r____ V...('variable b is incorrect') fr.. N..
#
# # else
# ___ divide_numbers
#     w____ T..
#         ___
#             first_number _ float(input('First number: '))
#             second_number _ float(input('Second number: '))
#             result _ first_number / second_number
#         _____ V... Z..... a_ error
#             print('Error:', ?)
#             print('Please t__ again')
#             print()
#         ____
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
#     __ ? __ 'y'
#         r____ E..
#
#
# ___
#     ?
# _____
#     print('Exception handler')
# f_____
#     print('Finally block')
#
# # t__-finally
# ___
#     2 / 0
# f____
#     print('Finally block is always executed')
