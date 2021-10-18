# ____ m.. ______ U..
#
#
# c_ TestUserModel
#     ___ setup_method  method
#         p..
#
#     ??
#     ___ setup_class ___
#         p..
#
#     ??
#     ___ teardown_class ___
#         p..
#
#     ___ test_constructor
#         user _ ? 'e@example.com' 't1' 't2'
#         a.. ?.f.. __ 't1'
#         a.. ?.l.. __ 't2'
#         a.. ?.e.. __ 'e@example.com'
#
#     ___ test_str  user
#         pattern _ 'User: <|i.: |n..>'
#         a.. st.(?) __ ?.f.. i_u_.i
#                                            n_u_.g..
#
#     ___ test_full_name  user
#         pattern _ '{} {}'
#         a.. ?.g.. __ \
#                ?.f.. ?.f.. ?.l..
#
# c_ TestUserModel2:
#
#     ___ test_str  user, post
#         p..
#
#     ___ test_full_name  user, post
#         p..
