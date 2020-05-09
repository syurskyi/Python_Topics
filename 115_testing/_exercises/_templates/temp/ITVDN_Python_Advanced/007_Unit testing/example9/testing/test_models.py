# ______ d_t_
#
# ____ m.. ______ U..
#
#
# ___ setup_method  method
#     r_ V..
#
#
# c_ TestUserModel
#     ___ setup_method  method
#         p..
#
#     ___ teardown_method  method
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
#         user _ U.. 'e@example.com' 't1' 't2'
#         a.. ?.f.. __ 't1'
#         a.. ?.l.. __ 't2'
#         a.. ?.e.. __ 'e@example.com'
#
#     ___ test_str  user
#         pattern _ 'User: <|i.: |n..>'
#         a.. st.(?) __ ?.f.. i_u__.i.
#                                            n_u__.g..
#
#     ___ test_full_name  user
#         pattern _ '{} {}'
#         a.. ?.g.. __ \
#                ?.f..(?.f.. ?.l..
#
#
# c_ TestUserModel2:
#
#     ___ test_constructor
#         user _ U.. 'e@example.com' 't1' 't2'
#         a.. ?.f.. __ 't1'
#         a.. ?.l.. __ 't2'
#         a.. ?.e.. __ 'e@example.com'
#
#     ___ test_str  user
#         pattern _ 'User: < i.: |n..>'
#         a.. st.(?) __ ?.f.. i_u_.i
#                                            n_u_.g..
#
#     ___ test_full_name  user
#         pattern _ '{} {}'
#         a.. ?.g.. __ \
#                ?.f.. ?.f.. ?.l..
#
#     ___ test_list
#         a.. [1, 2, 3] __ [1, 2, 3]
#         # assert [1, 2, 3] == [1, 2, 4]
#
#     ___ test_mocker  mocker
#         mocked_dt _ ?.pa..  'datetime.datetime'
#         ?.no_.r_v.. _ 1
#         a.. d_t_.d_t_.n.. __ 1
#         a.. [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 20, 3, 4, 5] __ \
#                [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
