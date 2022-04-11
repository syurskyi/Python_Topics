# ____ c.. _______ n..
#
# User  n.. 'User', 'name role expired'
# USER, ADMIN  'user', 'admin'
# SECRET  'I am a very secret token'
#
# julian  User name_'Julian', role_USER, expired_F..
# bob  User(name_'Bob', role_USER, expired_T..)
# pybites  User(name_'PyBites', role_ADMIN, expired_F..)
# USERS  ? ? ?
#
# # define exception classes here
# c_ UserDoesNotExist E..
#     p..
#
# c_ UserAccessExpired E..
#     p..
#
# c_ UserNoPermission E..
#     p..
#
# ___ get_secret_token username
#
#     users  user.n.. ___ ? __ ?
#
#     __ ? n.. __ ?
#         r.. ?
#
#     ___ user __ ?
#         __ ? __ ?.n..
#             __ ?.e.. __ T..
#                 r.. U..
#             __ ?.r.. !_ A..
#                 r.. U..
#
#             r.. ?
#
# # if __name__ == "__main__":
# #     print(get_secret_token("Bob"))