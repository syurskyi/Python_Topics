# ######################################################################################################################
# Decorators with parameters
# user_has_permission

# i_ f_
#
# user = {'username': 'jose123', 'access_level': 'user'}
#
# ___ user_has_permission access_level
#     ___ my_decorator func
#         func__.wr__ func
#         ___ secure_func panel
#             __ user.g__('access_level') __ access_level
#                 r_ func panel
#         r_ secure_func
#     r_ my_decorator
#
# _user_has_permission 'user'
# ___ my_function panel
#     """
#     Allows us to retrieve the password for the admin panel.
#     """
#     r_ _'Password for |panel| panel is 1234.'
#
# print(my_function.__n_
# print(my_function('movies'))
#
# print()