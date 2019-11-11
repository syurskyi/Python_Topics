# ######################################################################################################################
#  Generic decorators for any function
# user_has_permission

# i_ f_
#
# user = {'username': 'jose123', 'access_level': 'admin'}
#
# ___ user_has_permission func
#     _fun___.wr__ func
#     ___ secure_func _args __kwargs
#         __ user.g_('access_level') __ 'admin'
#             r_ func _args __kwargs
#     r_ secure_func
#
# _user_has_permission
# ___ my_function panel
#     """
#     Allows us to retrieve the password for the admin panel.
#     """
#     r_ _'Password for |panel| panel is 1234.'
#
# _user_has_permission
# ___ another
#     pass
#
# print(my_function.__n_
#
# print(my_function('movies'))
# print(another())
#
# print()