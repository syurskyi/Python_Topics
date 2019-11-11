# Using a @syntax
# user_has_permission

# user = {'username': 'jose123', 'access_level': 'guest'}
#
# ___ user_has_permission func
#     ___ secure_func
#         __ user.g_ 'access_level' __ 'admin'
#             r_ func
#     r_ se__f_
#
# _user_has_permission
# ___ my_function
#     """
#     Allows us to retrieve the password for the admin panel.
#     """
#     r_ 'Password for admin panel is 1234.'
#
# _user_has_permission
# ___ another
#     pass
#
# print my_function.__n_
# print another.__n_
#
# print()